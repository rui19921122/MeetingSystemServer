from django.conf.urls import url
from .views import GetAttendTableView,ReplaceAttentionWorkerView

urlpatterns = [
    url(r'get-attend-table/(?P<department>\d{1,3})/(?P<date>\d{4}-\d{1,2}-\d{1,2})/(?P<day_number>[12])/',
        GetAttendTableView.as_view(), name='get-attend-table'),
    url(r'change-worker/(?P<pk>\d{1,10})/',
        ReplaceAttentionWorkerView.as_view(), name='change-worker'),
]
