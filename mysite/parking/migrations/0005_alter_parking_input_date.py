# Generated by Django 3.2.3 on 2021-11-01 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_auto_20211101_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='input_date',
            field=models.TimeField(default=datetime.datetime(2021, 11, 1, 11, 32, 54, 763966), editable=False, help_text='Date Event'),
        ),
    ]