# Generated by Django 3.2.3 on 2021-11-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0011_auto_20211101_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelparking',
            name='input_date',
            field=models.DateTimeField(default='01/11/2021 13:01:1635771680s \tt', editable=False, help_text='Date Event'),
        ),
    ]