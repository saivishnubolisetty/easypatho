# Generated by Django 2.0.5 on 2018-06-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypathoapp', '0002_auto_20180603_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccpr',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]