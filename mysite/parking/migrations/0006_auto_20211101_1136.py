# Generated by Django 3.2.3 on 2021-11-01 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0005_alter_parking_input_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelParking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_places_parking', models.CharField(help_text='How many parking available you have seen', max_length=200)),
                ('input_date', models.TimeField(default=datetime.datetime(2021, 11, 1, 11, 36, 13, 546157), editable=False, help_text='Date Event')),
                ('parking_day_date', models.DateTimeField(default='01/11/2021', help_text='Please pick up the date')),
                ('user_name', models.CharField(default='cwayacita', editable=False, help_text='Your user', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='parking',
        ),
    ]
