# Generated by Django 3.0.14 on 2022-01-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0007_managerusercompetition_scorecompetition'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListTopticCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=80)),
                ('file_excel', models.FileField(upload_to='game/topic/')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerCalculateRankingPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank1', models.PositiveSmallIntegerField(default=0)),
                ('rank2', models.PositiveSmallIntegerField(default=0)),
                ('rank3', models.PositiveSmallIntegerField(default=0)),
                ('rank4_onwards', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TopicOfClassCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_topic', models.IntegerField(choices=[(3, 'Lớp 3'), (4, 'Lớp 4'), (5, 'Lớp 5'), (6, 'Lớp 6'), (7, 'Lớp 7'), (8, 'Lớp 8')], default=3)),
                ('list_topic', models.ManyToManyField(blank=True, related_name='listTopic', to='competition.ListTopticCompetition')),
            ],
        ),
    ]
