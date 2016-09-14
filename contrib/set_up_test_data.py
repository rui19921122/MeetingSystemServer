from django.contrib.auth.models import User

from base.models import Department, Job
from person.models import SystemUser, Worker


def set_up_normal_data():
    test_department = Department(department_name='测试部门')
    test_department.save()
    user = User.objects.create_user(username='测试用户', password='111111')
    system_user = SystemUser(user=user, department=test_department, name='测试用户名')
    system_user.save()
