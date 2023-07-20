from django.shortcuts import render
from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Note, User
from django.contrib.auth.decorators import login_required


# Create your views here.

def add_note(request, username):

    if request.method == 'GET':
        username = username
        response = '未回复'  #这里切换到数据库
        return render(request, 'add_note.html', locals())

    elif request.method == 'POST':
        #处理数据
        user = User.objects.get(username=username)
        title = request.POST['title']
        content = request.POST['content']

        Note.objects.create(title=title, content=content, user_id=user.id)
        return HttpResponseRedirect('/note/' + username +'/all')


def list_view(request, username):
    if request.method =='GET':
        username = username
        user = User.objects.get(username=username)
        # 1.all_notes = user.note_set.all()
        # 2.
        all_notes = Note.objects.filter(is_delete=False, user_id=user.id)   #  关键！！！
        # all_notes = Note.objects.filter(is_delete=False)

        return render(request, 'list_note.html', locals())




def update_view(request, note_id):
    try:
        note = Note.objects.get(id=note_id, is_delete=False)
        username = User.objects.get(id=note.user_id).username

    except Exception as e:
        print('--update error is %s'%(e))
        return HttpResponse('日记不存在')


    if request.method == 'GET':
        content = note.content
        title = note.title
        return render(request, 'update_note.html', locals())

    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect('/note/' + username + '/all')



def delete_view(request, note_id):
    if not note_id:
        return HttpResponse('请求异常')
    try:
        note = Note.objects.get(id=note_id, is_delete=False)
        username = User.objects.get(id=note.user_id).username
    except Exception as e:
        print('delete error is %s'%(e))
        return HttpResponse('--The note id is error')
    note.is_delete = True
    note.save()
    return HttpResponseRedirect('/note/' + username + '/all')



