# Generated by Django 3.2 on 2023-04-02 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_user_username_email'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='username_email',
        ),
    ]
