# Generated by Django 3.1.7 on 2021-04-14 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wbvs', '0013_history_voted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='voted',
        ),
    ]