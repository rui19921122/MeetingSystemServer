from django.core.urlresolvers import reverse
from base.models import ClassNumberTable, Department
from rest_framework.test import APITestCase
from contrib.set_up_test_data import set_up_normal_data
from person.models import Worker
from person.serializers import WorkerSer
from attend.serializers import AttendPersonSer
from attend.models import AttendTable, AttendPerson


# Create your tests here.

class TestBaseAttend(APITestCase):
    def setUp(self):
        set_up_normal_data()

    def test_get_attend_table_data_without_created(self):
        """
        测试获取出勤表情况(未提前建表)
        :return:
        """
        department_id = Department.objects.get(department_name='test').id
        url = reverse("get-attend-table",
                      kwargs={'date': '2016-09-17',
                              'day_number': 1,
                              'department': department_id
                              })
        self.client.login(username='test_user', password='111111')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data.get('all_workers'),
                         WorkerSer(Worker.objects.all(), many=True).data,
                         data.get('all_workers'))

        self.assertEqual(len(data.get('attend_workers')),
                         1
                         )

    def test_get_attend_table_data_with_created(self):
        """
        测试获取出勤表情况(提前建表)
        :return:
        """
        department_id = Department.objects.get(department_name='test').id
        url = reverse("get-attend-table",
                      kwargs={'date': '2016-09-17',
                              'day_number': 1,
                              'department': department_id
                              })
        self.client.login(username='test_user', password='111111')
        self.client.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data.get('all_workers'),
                         WorkerSer(Worker.objects.all(), many=True).data,
                         data.get('all_workers'))

        self.assertEqual(len(data.get('attend_workers')),
                         1
                         )


class UpdateWorkerAttention(APITestCase):
    def setUp(self):
        set_up_normal_data()
        self.client.login(username='test_user', password='111111')
        self.department_id = Department.objects.get(department_name='test').id

    def test_normal_worker_replace(self):
        """
        测试正常的职工替换（非学员）
        :return:
        """
        ori_url = reverse("get-attend-table",
                          kwargs={'date': '2016-09-17',
                                  'day_number': 1,
                                  'department': self.department_id
                                  })
        self.client.login(username='test_user', password='111111')
        response = self.client.get(ori_url)
        json = response.json()
        self.assertIsInstance(json, dict)
        for worker in json.get('attend_workers'):
            if not worker.get('is_study'):
                url = worker.get('url')
                res = self.client.put(url, data={'worker': json.get('all_workers')[0]['id']})
                self.assertEqual(res.status_code, 200)
                self.assertEqual(res.json().get('worker'), json.get('all_workers')[0]['worker_name'])
                continue

    def test_normal_worker_delete(self):
        """
        测试正常的职工删除（非学员），不应成功
        :return:
        """
        ori_url = reverse("get-attend-table",
                          kwargs={'date': '2016-09-17',
                                  'day_number': 1,
                                  'department': self.department_id
                                  })
        self.client.login(username='test_user', password='111111')
        response = self.client.get(ori_url)
        json = response.json()
        self.assertIsInstance(json, dict)
        for worker in json.get('attend_workers'):
            if not worker.get('is_study'):
                url = worker.get('url')
                res = self.client.delete(url)
                self.assertNotEqual(res.status_code, 200)
                continue