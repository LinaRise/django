# Generated by Django 2.2.16 on 2020-10-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20201030_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='group',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='interests',
            field=models.TextField(),
        ),
    ]
