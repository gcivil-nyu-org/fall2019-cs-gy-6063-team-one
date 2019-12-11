from django.db import models
from uplyft.models import CustomUser

# Create your models here.


class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ENTITY_TYPE_APPLICATION_REJECTED = "ARJ"
    ENTITY_TYPE_APPLICATION_REVIEWED = "ARV"
    ENTITY_TYPE_APPLICATION_ADVANCED = "AAD"
    ENTITY_TYPE_APPLICATION_RECEIVED = "ARC"
    ENTITY_TYPE_APPLICATION_WITHDRAWN = "AWD"
    ENTITY_TYPES = [
        (ENTITY_TYPE_APPLICATION_REJECTED, "Application Rejected"),
        (ENTITY_TYPE_APPLICATION_REVIEWED, "Application Reviewed"),
        (ENTITY_TYPE_APPLICATION_ADVANCED, "Application Advanced"),
        (ENTITY_TYPE_APPLICATION_RECEIVED, "Application Received"),
        (ENTITY_TYPE_APPLICATION_WITHDRAWN, "Application Withdrawn"),
    ]
    STATUS_UNREAD = "UNRD"
    STATUS_READ = "READ"
    STATUSES = [(STATUS_UNREAD, "Unread"), (STATUS_READ, "Read")]
    entity_type = models.CharField(
        max_length=3, choices=ENTITY_TYPES, blank=False, null=False
    )
    entity_fk_pk = models.PositiveIntegerField(blank=False, null=False)
    status = models.CharField(
        max_length=4, choices=STATUSES, blank=False, null=False, default=STATUS_UNREAD
    )
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
