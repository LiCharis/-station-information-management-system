from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Duty
from django.contrib.auth.decorators import login_required

# Create your views here.

def add_note(request, username):

    if request.method == 'GET':
        username = username
        response = '未回复'  # 这里切换到数据库
        return render(request, 'add_info.html', locals())

    elif request.method == 'POST':
        #处理数据
        user = User.objects.get(username=username)
        flow = request.POST['flow']
        rate = request.POST['rate']
        condition = request.POST['condition']
        attendance = request.POST['attendance']
        emergency = request.POST['emergency']
        clear = request.POST['clear']

        Duty.objects.create(flow=flow, rate=rate, condition=condition, attendance=attendance, emergency=emergency, clear=clear,  user_id=user.id)
        return HttpResponseRedirect('/duty/' + username +'/all')


def list_view(request, username):
    if request.method =='GET':
        username = username
        user = User.objects.get(username=username)
        # 1.all_notes = user.note_set.all()
        # 2.
        all_duties = Duty.objects.filter(is_delete=False, user_id=user.id)   #  关键！！！
        # all_notes = Note.objects.filter(is_delete=False)

        return render(request, 'list_info.html', locals())



def update_view(request, duty_id):
    try:
        duty = Duty.objects.get(id=duty_id, is_delete=False)
        username = User.objects.get(id=duty.user_id).username

    except Exception as e:
        print('--update error is %s'%(e))
        return HttpResponse('日记不存在')


    if request.method == 'GET':
        flow = duty.flow
        rate = duty.rate
        condition = duty.condition
        attendance = duty.attendance
        emergency = duty.emergency
        clear = duty.clear
        response = duty.response

        return render(request, 'update_info.html', locals())

    elif request.method == 'POST':

        flow = request.POST['flow']
        rate = request.POST['rate']
        condition = request.POST['condition']
        attendance = request.POST['attendance']
        emergency = request.POST['emergency']
        clear = request.POST['clear']

        duty.flow = flow
        duty.rate = rate
        duty.condition = condition
        duty.attendance = attendance
        duty.emergency = emergency
        duty.clear = clear

        duty.save()

        return HttpResponseRedirect('/duty/' + username + '/all')



def delete_view(request, duty_id):
    if not duty_id:
        return HttpResponse('请求异常')
    try:
        duty = Duty.objects.get(id=duty_id, is_delete=False)
        username = User.objects.get(id=duty.user_id).username
    except Exception as e:
        print('delete error is %s'%(e))
        return HttpResponse('--The note id is error')
    duty.is_delete = True
    duty.save()
    return HttpResponseRedirect('/duty/' + username + '/all')



