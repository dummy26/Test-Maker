# Generated by Django 3.1.7 on 2021-03-19 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.IntegerField(null=True),
        ),
    ]
