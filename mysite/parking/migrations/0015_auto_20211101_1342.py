# Generated by Django 3.2.3 on 2021-11-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0014_alter_modelparking_input_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_day_date', models.DateTimeField(default='2021-11-01', help_text='Please pick up the date')),
            ],
            options={
                'ordering': ('-search_day_date',),
            },
        ),
        migrations.AlterField(
            model_name='modelparking',
            name='input_date',
            field=models.DateTimeField(default='2021-11-01 13:42', editable=False, help_text='Date Event'),
        ),
        migrations.AlterField(
            model_name='modelparking',
            name='parking_day_date',
            field=models.DateTimeField(default='2021-11-01', help_text='Please pick up the date'),
        ),
    ]