
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Teacher,Student
from django.contrib.auth.models import User

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
import json
# 引入装饰器函数

# Create your views here.
'''
def login(request):
    if request.method == "POST":
        Accountname = request.POST.get('Account', None)
        password = request.POST.get('Password', None)
        if Accountname and password:  # 确保用户名和密码都不为空
            Accountname = Accountname.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                #user = models.login_user.objects.get(Account=Accountname)
                user = User.objects.get(Account=Accountname)
                print(user)
            except:
                #return render(request, 'login/login.html')
                return HttpResponse('EXCEPT')
            if user.Password == password:
                return redirect('/index/')
               # return HttpResponse('登陆成功')
    #return render(request, 'login/login.html')
    return HttpResponse('你不是POST')
'''

def Get_UserType(username):
    # UserType=Teacher.objects.get(tno=username)
    try:
        UserType = Teacher.objects.get(tno=username)
        return 'T'
    except Teacher.DoesNotExist:
        try:
            UserType = Student.objects.get(sno=username)
            return 'S'
        except Student.DoesNotExist:
            return None

def reg():
    user = User.objects.create_user(100,None,'123')
    user.save()
    return None


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    data=json.loads(request.body.decode('utf-8'))
    username = data.get('username')
    password = data.get('password')
    # UserType=Get_UserType(username)
    if username and password :
        user_obj = auth.authenticate(username=username, password=password)
        # print(user_obj.username)
        if not user_obj:
            return HttpResponse('账号密码错误')
        else:#成功登陆
            auth.login(request, user_obj)
            UserType=Get_UserType(username)
            data={
                'UserType':UserType
            }
            return JsonResponse(data)
            # if UserType=='S':
            #     # auth.login(request, user_obj)
            #     return redirect('/index/')
            # else:
            #     return redirect('/teacher/')
    else:
        return HttpResponse('账号密码不能为空')
