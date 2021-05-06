from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import auth
from django.contrib.auth.models import User
# 引入装饰器函数
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    user = User.objects.get(username=request.user.username)
    print(user)
    return render(request, 'index.html')