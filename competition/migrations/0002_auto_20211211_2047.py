# Generated by Django 3.0.14 on 2021-12-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='typecompetition',
            name='description',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='typecompetition',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
