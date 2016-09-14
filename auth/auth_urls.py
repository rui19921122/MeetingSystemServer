from django.conf.urls import url
from .views import BaseLoginInView,LoginOutView,ChangePasswordView

urlpatterns = [
    url(r'base-login/', BaseLoginInView.as_view(), name='base-login'),
    url(r'logout/', LoginOutView.as_view(), name='logout'),
    url(r'change-password/', ChangePasswordView.as_view(), name='change-password'),
]
