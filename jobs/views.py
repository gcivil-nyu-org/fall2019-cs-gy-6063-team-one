import csv
from datetime import datetime
from django.contrib import messages
import logging
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Job


def dummy_jobs(request):
    numbers_list = range(1, 1000)

    page = request.GET.get("page", 1)

    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, "jobs/dummy_jobs.html", {"numbers": numbers})


class JobsView(ListView):
    model = Job
    paginate_by = 10
    ordering = ["-posting_date"]
    context_object_name = "jobs"
    template_name = "jobs/jobs.html"
    queryset = Job.objects.all()


logger = logging.getLogger(__name__)


def jobs(request):
    return render(request, "jobs/jobs.html")


def load_jobs(request):
    if request.method == "POST":
        with open("jobs/NYC_Jobs.csv", encoding="UTF-8") as csvfile:
            read_csv = csv.reader(csvfile, delimiter=",")
            for i, x in enumerate(read_csv):
                logger.info("Importing value: " + str(i))
                if i != 0:
                    for j, field in enumerate(x):
                        if j > 22 and j != 24 and x[j]:
                            x[j] = datetime.strptime(x[j], "%m/%d/%Y").strftime(
                                "%Y-%m-%d"
                            )
                        if j == 24 and x[j]:
                            x[j] = datetime.strptime(
                                x[j], "%Y-%m-%dT%H:%M:%S.%f"
                            ).strftime("%Y-%m-%d")
                        if j > 22 and not x[j]:
                            x[j] = None
                    job = Job(
                        job_id=x[0],
                        agency=x[1],
                        posting_type=x[2],
                        business_title=x[3],
                        civil_service_title=x[4],
                        title_code_no=x[5],
                        level=x[6],
                        job_category=x[7],
                        ft_pt_indicator=x[8],
                        salary_start=x[9],
                        salary_end=x[10],
                        salary_frequency=x[11],
                        work_location=x[12],
                        division=x[13],
                        job_description=x[14],
                        min_qualifications=x[15],
                        preferred_skills=x[16],
                        additional_info=x[17],
                        to_apply=x[18],
                        hours_info=x[19],
                        secondary_work_location=x[20],
                        recruitment_contact=x[21],
                        residency_requirement=x[22],
                        posting_date=x[23],
                        post_until=x[24],
                        posting_updated=x[25],
                        process_date=x[26],
                    )
                    job.save()
            messages.success(request, "Jobs imported successfully")
            return render(request, "jobs/jobs_import.html")
    else:
        return render(request, "jobs/jobs_import.html")
