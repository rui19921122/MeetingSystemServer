from django.contrib.auth.models import User
from script.add_class_number_to_database import start

from base.models import Department, Job
from person.models import SystemUser, Worker


def set_up_normal_data():
    start(number=100)
    test_department = Department(department_name='test')
    test_department.save()
    user = User.objects.create_user(username='test_user', password='111111')
    system_user = SystemUser(user=user, department=test_department, name='test_user名')
    system_user.save()
    job_1 = Job(job_name="test_job_1", should_attend_meeting=True,department=test_department)
    job_1.save()
    job_2 = Job(job_name="test_job_2", should_attend_meeting=True,department=test_department)
    job_2.save()
    worker_1 = Worker(class_number='1', is_study=False, job=job_1,
                      department=test_department,
                      worker_name='test_worker_1')
    worker_1.save()
    worker_2 = Worker(class_number='2', is_study=False, job=job_1,
                      department=test_department,
                      worker_name='test_worker_2')
    worker_2.save()
    worker_3 = Worker(class_number='3', is_study=False, job=job_2,
                      department=test_department,
                      worker_name='test_worker_3')
    worker_3.save()
    worker_4 = Worker(class_number='4', is_study=False, job=job_2,
                      department=test_department,
                      worker_name='test_worker_4')
    worker_4.save()
