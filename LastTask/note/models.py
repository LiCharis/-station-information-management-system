from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='反馈内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_delete = models.BooleanField(verbose_name='是否已删除', default=False)
    response = models.TextField(verbose_name='回复', default='等待回复')

    class Meta:
        verbose_name = 'notes'
        db_table = 'notes'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s-%s-%s'%(self.user,self.title,self.content)




