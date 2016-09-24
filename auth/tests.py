from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from base.models import Department, Job
from person.models import SystemUser, Worker
from contrib.set_up_test_data import set_up_normal_data


# Create your tests here.
class TestAuthLoginBase(APITestCase):
    """
    测试基本的登陆、下线、更改密码功能,由于权限设置，因此无法创建用户
    """

    def setUp(self):
        set_up_normal_data()

    def test_login(self):
        data = {'username': 'test_user', 'password': '111111'}
        url = reverse("base-login")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200, response.data)

    def test_logout(self):
        url = reverse('logout')
        self.client.login(username='test_user',
                          password='111111')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200, response.data)

    def test_change_password(self):
        url = reverse("change-password")
        self.client.login(username='test_user',
                          password='111111')
        data = {'password': '222222'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(username="test_user").check_password('222222'), True)
