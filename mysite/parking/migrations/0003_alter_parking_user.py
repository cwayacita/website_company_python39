# Generated by Django 3.2.3 on 2021-11-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20211101_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='user',
            field=models.CharField(editable=False, max_length=200),
        ),
    ]
