# Generated by Django 3.1.7 on 2021-04-12 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wbvs', '0009_user_dp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dp',
            new_name='image',
        ),
    ]