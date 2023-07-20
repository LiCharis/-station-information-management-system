from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Duty(models.Model):

    create_time = models.DateTimeField(verbose_name='时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    flow = models.CharField(verbose_name='客流量', max_length=100)
    rate = models.CharField(verbose_name='准点率', max_length=100)
    condition = models.CharField(verbose_name='车辆情况', max_length=100)
    attendance = models.CharField(verbose_name='员工考勤', max_length=100)
    emergency = models.CharField(verbose_name='紧急情况', max_length=100)
    clear = models.CharField(verbose_name='环境整洁和设施维护', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_delete = models.BooleanField(verbose_name='是否已删除', default=False)
    response = models.TextField(verbose_name='领导回复', default='等待领导的回复')


    class Meta:
        verbose_name = 'duties'
        db_table = 'duties'
        verbose_name_plural = verbose_name

   



