# Generated by Django 3.1.7 on 2021-03-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20210318_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='timeLimit',
            field=models.IntegerField(null=True),
        ),
    ]
