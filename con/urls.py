from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^test/$', views.Test.as_view(), name='test'),
]