from django.urls import path
from index import views
from django.conf.urls import url

urlpatterns = [
    url(r'',views.index),
]