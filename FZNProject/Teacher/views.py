from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count,F
from .models import Teacher,Student,St
import json
# from .models import FST
# 引入装饰器函数
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login/')
def Teacher_page(request):  #教师页面的展示
    user = User.objects.get(username=request.user.username)
    # print(user)
    # user='1'  #教师的名称
    return HttpResponse(user)

def Teacher_MyStudent(request):#查询选择了教师的学生信息
    data = json.loads(request.body.decode('utf-8'))
    user = data.get("tID")
    Student_Number=St.objects.filter(tno=user).count() #查询选择了的学生人数
    if Student_Number == 0:
        return  HttpResponse('no data')
    Students=St.objects.filter(tno=user) #查询选择了的学生的信息 sno和sname
    StudentsJson = []
    for Student_i in Students:
        StudentsJson.append({
                'Sno':Student_i.sno,
                'Sname':Student_i.sname,
        })
    data={
        'list':StudentsJson,
        'number':Student_Number
    }
    return JsonResponse(data,safe=False)


def Teacher_Information(request): #获取教师个人信息
    data = json.loads(request.body.decode('utf-8'))
    Teacher_tno = data.get("username")
    TeacherInformation=Teacher.objects.get(tno=Teacher_tno)
    data={
        'tname':TeacherInformation.tname,
        'Sex':TeacherInformation.sex,
        'Pro':TeacherInformation.pro,
        'number':TeacherInformation.number,
        'Contact':TeacherInformation.contact,
        'D_information':TeacherInformation.d_information,
        'state':TeacherInformation.state,
        'Tno':TeacherInformation.tno

    }
    return JsonResponse(data)

def Teacher_InfomationChange(request): #修改教师个人信息
    data = json.loads(request.body.decode('utf-8'))
    Teacher_tno = data.get("username")
    Teacher_info_new=data.get("info") #获取评价
    Teacher_info_new_contact=data.get("contact")
    Teacher_info=Teacher.objects.get(tno=Teacher_tno) #获取object
    Teacher_info.d_information=Teacher_info_new #修改object
    Teacher_info.contact=Teacher_info_new_contact
    Teacher_info.save() #确认修改
    return HttpResponse('成功修改信息')

def Teacher_SelectStudent(request): #选择学生
    SelectSno=request.GET.getlist() #获取选择的学生的sno
    User_name = request.user.username
    User_tname = Teacher.objects.get(id=User_name).tname
    #设置数据表FST存储最终选择
    Teacher_ST=St()
    SlectNum=SelectSno.count
    for i in range(SlectNum) :
        Teacher_ST.sno=SelectSno[i].sno
        Teacher_ST.sname=SelectSno[i].same
        Teacher_ST.tno=User_name
        Teacher_ST.tname=User_tname
        Teacher_ST.save()
    return HttpResponse('选择成功')

def Teacher_SelectStudent_byone(request):#单个选择学生
    data = json.loads(request.body.decode('utf-8'))
    tno_get = data.get("tID")
    sno_get = data.get("sID")
    sname=Student.objects.get(sno=sno_get)
    FLAG = St.objects.filter(sno=sno_get).count()
    if FLAG == 1:
        return HttpResponse('该同学已经选择导师')
    tname=Teacher.objects.get(tno=tno_get)
    Teacher_ST=St()
    Teacher_ST.sno = sno_get
    Teacher_ST.sname = sname.sname
    Teacher_ST.tno = tno_get
    Teacher_ST.tname = tname.tname
    Teacher_ST.save()
    return HttpResponse('添加学生成功')

def ChangeNumber(request):#修改计划人数
    data = json.loads(request.body.decode('utf-8'))
    Newest_number=data.get("Newest_number")
    Teacher_tno = data.get("username")
    print(Newest_number)
    Teacher_numberchange= Teacher.objects.get(tno=Teacher_tno) #获取object
    Teacher_numberchange.number=Newest_number #修改object
    Teacher_numberchange.save()
    return HttpResponse('成功修改人数')

def DeleteStudent(request):
    data = json.loads(request.body.decode('utf-8'))
    DeleteSno = data.get("sID")
    SnoIndb = St.objects.filter(sno=DeleteSno).first()
    if SnoIndb:
        SnoIndb.delete()
        return HttpResponse('移除成功')
    else:
        return HttpResponse('出错了')

def LockList(request):
    data = json.loads(request.body.decode('utf-8'))
    User_name = data.get("tID")
    Teacher_lock =  Teacher.objects.get(tno=User_name)
    Teacher_lock.state=1
    Teacher_lock.save()
    return HttpResponse('成功锁定名单！')
