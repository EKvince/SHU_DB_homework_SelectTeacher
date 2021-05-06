from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.Student),
    url(r'^MyTeacher$',views.Student_MyTeacher),
    url(r'^Teacher_think$',views.Student_TeacherThink),
    url(r'^Teacher_Exchange$', views.Teacher_Exchange),
    url(r'^Teacher_Find$',views.Teacher_Find),
    url(r'^Teacher_DInformation$',views.Teacher_DInformation),
    url(r'^Student_Information$',views.Student_Information),
    url(r'^Student_Choose$',views.Teacher_Choose),
    url(r'^ChangeInfo$',views.Student_InfomationChange),
    url(r'^Comments$',views.Teacher_Comment)

]