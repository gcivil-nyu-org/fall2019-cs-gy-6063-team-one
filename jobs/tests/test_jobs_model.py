from django.test import TestCase
from uplyft.tests.resources import test_user_data, create_department
from jobs.models import Job, Department


class JobsModelTest(TestCase):
    def setUp(self):
        self.department = create_department(test_user_data["department"])
        job_details = test_user_data["job_details"]
        job_details[0]["department"] = self.department
        job_details[1]["department"] = self.department
        self.job1 = Job.objects.create(**job_details[0])
        self.job2 = Job.objects.create(**job_details[1])

    def test_eq_compare_to_null(self):
        self.assertFalse(self.job1.__eq__(None))

    def test__eq__compares_on_id_not_equal(self):
        self.assertFalse(self.job1.__eq__(self.job2))

    def test__eq__compares_on_id_equal(self):
        job1_retrieved_by_id = Job.objects.get(id=1)
        self.assertTrue(self.job1.__eq__(job1_retrieved_by_id))

    def test__ne__compares_on_id_equal(self):
        job1_retrieved_by_id = Job.objects.get(id=1)
        self.assertFalse(self.job1.__ne__(job1_retrieved_by_id))

    def test__ne__compares_on_id_not_equal(self):
        self.assertTrue(self.job1.__ne__(self.job2))

    def test__eq__compares_on_instance(self):
        self.assertFalse(self.job1.__eq__(self.department))


class DepartmentModelTest(TestCase):
    def setUp(self):
        self.department_details = test_user_data["department"]
        self.department = Department.objects.create(**self.department_details)

    def test__str__returns_name(self):
        self.assertTrue(self.department.__str__(), self.department_details["name"])