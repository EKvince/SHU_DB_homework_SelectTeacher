from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import auth
from django.db.models import Count,F,Q
from .models import St,Teacher,Student,Comments,SMajor
#from .models import Teacher,Comment
# from .models import Teacher
import json
# 引入装饰器函数
from django.contrib.auth.decorators import login_required



def Student_MyTeacher(request): #查看导师信息
    data = json.loads(request.body.decode('utf-8'))
    My_sno = data.get("username")
    My_teacher_num = St.objects.filter(sno=My_sno).count()
    if My_teacher_num ==0 :
        return HttpResponse('no data')
    My_teacher_tno = St.objects.get(sno=My_sno).tno
    TeacherInfo = Teacher.objects.get(tno=My_teacher_tno)
    data={
        'name': TeacherInfo.tname,
        'sex': TeacherInfo.sex,
        'pro': TeacherInfo.pro,
        'number': TeacherInfo.number,
        'D_information': TeacherInfo.d_information,
        'id': TeacherInfo.tno,
        'Contact': TeacherInfo.contact,
        'state':TeacherInfo.state
    }
    return JsonResponse(data)

def Student_TeacherThink(request): #导师评论
    data = json.loads(request.body.decode('utf-8'))
    Sno_get = data.get("sID")
    Tno_get = data.get("tID")
    Sno_comment = data.get("comment")
    Choose_judge = St.objects.filter(Q(sno=Sno_get) & Q(tno=Tno_get)).count()
    Think = Comments()
    Sno_get_num = Comments.objects.filter(Q(sno=Sno_get) & Q(tno=Tno_get)).count()
    if Choose_judge == 0:
        return HttpResponse('你未选择该导师，无法评论')
    if Sno_get_num == 1:
        return HttpResponse('已经评论过了')
    Think.tno = Tno_get
    Think.message = Sno_comment
    Think.sno = Sno_get
    Think.save()
    return HttpResponse('评论成功')

def Teacher_Exchange(request): #退选导师
    data = json.loads(request.body.decode('utf-8'))
    DeleteSno = data.get("sID")
    SnoIndb = St.objects.filter(sno=DeleteSno).first()
    if SnoIndb:
        SnoIndb.delete()
        return HttpResponse('移除成功')
    else:
        return HttpResponse('出错了')

def Student_Information(request): #显示学生个人信息
    data = json.loads(request.body.decode('utf-8'))
    Student_sno = data.get("username")
    SInformation=Student.objects.get(sno=Student_sno)
    Student_mtext = SMajor.objects.get(mno=SInformation.mno)
    data = {
        'Sname': SInformation.sname,
        'Sex': SInformation.sex,
        'Mtext': Student_mtext.mtext,
        'Contact': SInformation.contact,
        'grade':SInformation.gpa
    }
    return JsonResponse(data)

def Student_InfomationChange(request): #修改学生个人信息（联系方式）
    data = json.loads(request.body.decode('utf-8'))
    Student_sno = data.get("username")
    Student_info_new_contact = data.get("contact")
    print(Student_info_new_contact)
    Student_info=Student.objects.get(sno=Student_sno) #获取object
    Student_info.contact=Student_info_new_contact #修改object,仅修改联系方式
    Student_info.save() #确认修改
    return HttpResponse('成功修改信息')

def Teacher_Find(request): #查询相关导师
    data = json.loads(request.body.decode('utf-8'))
    Tname = data.get("Tname")
    T=Teacher.objects.get(tname=Tname) #查找符合条件的教师对象T
    now = St.objects.filter(tno=T.tno).count()
    data={
        'name': T.tname,
        'sex': T.sex,
        'pro': T.pro,
        'id': T.tno,
        'number': T.number,
        'D_information': T.d_information,
        'Contact': T.contact,
        'state':T.state,
        'Count': now
    }
    return JsonResponse(data)

def Teacher_DInformation(request): #显示导师详细信息
    # Teacher_tno=request.user.username
    Teacher_tno = 1
    TeacherInformation = Teacher.objects.filter(tno=Teacher_tno)
    print(TeacherInformation)
    return HttpResponse('信息显示成功')

def Teacher_Choose(request): #选择导师
    data = json.loads(request.body.decode('utf-8'))
    tno_get = data.get("tID")
    sno_get = data.get("sID")
    sname = Student.objects.get(sno=sno_get)
    FLAG = St.objects.filter(sno=sno_get).count()
    if FLAG == 1:
        return HttpResponse('你已经选择导师')
    tname = Teacher.objects.get(tno=tno_get)
    if tname.state == 1:
        return HttpResponse('该导师已经锁定名单！')
    Teacher_ST = St()
    Teacher_ST.sno = sno_get
    Teacher_ST.sname = sname.sname
    Teacher_ST.tno = tno_get
    Teacher_ST.tname = tname.tname
    Teacher_ST.save()
    return HttpResponse('导师选择成功')

def Teacher_Comment(request): #查看评论
    data = json.loads(request.body.decode('utf-8'))
    Teacher_tno = data.get("tID")
    TeacherComment=Comments.objects.filter(tno=Teacher_tno)
    CommentList=[]
    for comment_i in TeacherComment:
        CommentList.append({
            'message': comment_i.message,
            'sno': comment_i.sno
        })
    return JsonResponse(CommentList,safe=False)


