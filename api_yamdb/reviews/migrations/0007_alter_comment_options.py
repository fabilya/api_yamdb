# Generated by Django 3.2 on 2023-04-03 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20230403_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'default_related_name': '%(class)ss', 'ordering': ('-pub_date',), 'verbose_name': 'комментарий', 'verbose_name_plural': 'комментарии'},
        ),
    ]