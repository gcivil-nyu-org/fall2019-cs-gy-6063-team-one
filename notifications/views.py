from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Notification
from apply.models import Application


# Create your views here.
class NotificationCenterView(LoginRequiredMixin, ListView):
    model = Notification
    paginate_by = 10
    context_object_name = "notifications"
    template_name = "notifications/notification_center.html"

    def get_queryset(self):
        queryset = (
            Notification.objects.filter(
                Q(status=Notification.STATUS_UNREAD)
                | Q(status=Notification.STATUS_READ)
            )
            .filter(recipient=self.request.user)
            .order_by("-id")
        )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        context["Notification"] = Notification
        notifications = context["notifications"]

        notification_entities = {}
        for notification in notifications:
            if (
                notification.entity_type
                == Notification.ENTITY_TYPE_APPLICATION_REJECTED
                or notification.entity_type
                == Notification.ENTITY_TYPE_APPLICATION_ADVANCED
                or notification.entity_type
                == Notification.ENTITY_TYPE_APPLICATION_REVIEWED
                or notification.entity_type
                == Notification.ENTITY_TYPE_APPLICATION_RECEIVED
            ):
                application = Application.objects.get(id=notification.entity_fk_pk)
                notification_entities[notification.id] = (notification, application)
            else:
                pass
        context["entities"] = notification_entities
        print(notification_entities)

        return context


@login_required
def read_all(request):
    user = request.user
    Notification.objects.filter(recipient=user).update(status=Notification.STATUS_READ)

    return HttpResponseRedirect(reverse("notifications:notification_center"))
