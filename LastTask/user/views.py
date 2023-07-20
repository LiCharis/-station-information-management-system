import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def admin_jump(request):
    return HttpResponseRedirect('/admin')



def user_list(request):
    if request.method == 'GET':
        all_users = User.objects.filter(is_staff=True, is_superuser=False)
        return render(request, 'manager.html', locals())





def user_res_view(request, username):
    if request.method == 'POST':

        result = {"code": 200, "username": username}
        return JsonResponse(result)

def register_view(request):
    if request.method != 'POST':
        result = {"code": 205, "error": "Please use POST!"}
        return JsonResponse(result)

    elif request.method == 'POST':
        json_str = request.body
        json_dict = json.loads(json_str)
        username = json_dict['username']
        password_1 = json_dict['password_1']
        password_2 = json_dict['password_2']

        # 密码前后要保持一致
        if password_1 != password_2:
            result = {"code": 201, "error": "密码前后不一致"}
            return JsonResponse(result)

        old_users = User.objects.filter(username=username)
        if old_users:
            result = {"code": 202, "error": "用户名已注册"}
            return JsonResponse(result)

        #创建用户
        try:
            user = User.objects.create_user(username=username, password=password_1)
        except Exception as e:
            print('--create user error %s' % (e))
            result = {"code": 202, "error": "用户名已注册"}
            return JsonResponse(result)

        result = {"code": 200, "username": username}
        return JsonResponse(result)

def login_view(request):

    if request.method != 'POST':

        result = {"code": 205, "error": "please use POST！"}
        return JsonResponse(result)

    #处理用户名和密码
    elif request.method == 'POST':
        json_str = request.body
        json_dict = json.loads(json_str)
        is_staff = json_dict['is_staff']
        username = json_dict['username']
        password = json_dict['password']

        user = authenticate(username=username, password=password)

        if user.is_staff != is_staff:
            result = {"code": 204, "error": "登录身份不匹配!"}
            return JsonResponse(result)


        if not user:
            result = {"code": 203, "error": "用户名或者密码错误!"}
            return JsonResponse(result)

        else:
            #记录会话状态
            print(user)
            login(request, user)

            result = {"code": 200, "username": username}

            return JsonResponse(result)



def logout_view(request):

    logout(request)

    return HttpResponseRedirect('http://127.0.0.1:5000')






