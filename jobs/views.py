from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Job


def dummy_jobs(request):

    numbers_list = range(1, 1000)

    page = request.GET.get('page', 1)

    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'jobs/dummy_jobs.html', {'numbers': numbers})


class JobsView(ListView):
    model = Job
    paginate_by = 25
    context_object_name = 'jobs'
    template_name = 'jobs/jobs.html'


def generate_fake_data(request):
    from model_mommy import mommy
    mommy.make('jobs.Job', _quantity=50)
    return redirect('jobs')



