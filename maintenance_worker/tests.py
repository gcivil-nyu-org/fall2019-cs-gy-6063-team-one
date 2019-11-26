from django.test import TestCase
from maintenance_worker import manage_jobs, manage_demo_users


class MaintenanceWorkerExternalCallTest(TestCase):
    def test_manage_demo_users(self):
        manage_jobs.load_jobs()
        manage_demo_users.create_demo_employers()
        manage_demo_users.create_demo_candidates()
        manage_demo_users.reset_demo_employers()
        manage_demo_users.reset_demo_candidates()
        manage_demo_users.create_demo_candidates()
        manage_demo_users.create_demo_employers()
