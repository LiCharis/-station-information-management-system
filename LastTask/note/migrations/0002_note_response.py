# Generated by Django 4.0.5 on 2023-07-20 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='response',
            field=models.TextField(default='等待回复', verbose_name='回复'),
        ),
    ]
