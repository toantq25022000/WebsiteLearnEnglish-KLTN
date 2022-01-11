# Generated by Django 3.0.14 on 2022-01-03 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competition', '0006_auto_20211218_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_rank', models.CharField(default='', max_length=75)),
                ('points_title', models.PositiveSmallIntegerField(default=0)),
                ('timestart', models.DateTimeField()),
                ('type_compete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.TypeCompetition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerUserCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=75)),
                ('star_title', models.PositiveSmallIntegerField(default=1)),
                ('total_battle', models.PositiveSmallIntegerField(default=0)),
                ('win_1v1', models.PositiveSmallIntegerField(default=0)),
                ('win_1v9', models.PositiveSmallIntegerField(default=0)),
                ('total_title', models.PositiveSmallIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
