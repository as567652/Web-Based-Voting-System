# Generated by Django 3.1.7 on 2021-04-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbvs', '0016_history_voting_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booth',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
