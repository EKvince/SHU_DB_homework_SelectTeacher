from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.Teacher),
    url(r'^MyStudents$',views.Teacher_MyStudent),
    url(r'^MyInfo$',views.Teacher_Information),
    url(r'^ChangeNum$',views.ChangeNumber),
    url(r'^ChangeInfo$', views.Teacher_InfomationChange),
    url(r'^SelectStudent$', views.Teacher_SelectStudent_byone),
    url(r'^Remove$', views.DeleteStudent),
    url(r'^Lock$',views.LockList)

]