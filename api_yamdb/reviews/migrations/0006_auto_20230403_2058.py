# Generated by Django 3.2 on 2023-04-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20230403_0333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='code_is_used',
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='code', max_length=6, null=True, verbose_name='код подтверждения'),
        ),
    ]
