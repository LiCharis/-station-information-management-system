# Generated by Django 4.0.5 on 2023-07-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='response',
            field=models.TextField(default='等待领导的回复', verbose_name='领导回复'),
        ),
    ]
