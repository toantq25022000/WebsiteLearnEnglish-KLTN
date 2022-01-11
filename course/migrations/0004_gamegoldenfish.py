# Generated by Django 3.0.14 on 2021-12-07 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20211203_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameGoldenFish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_excel', models.FileField(upload_to='game/golden-fish/')),
                ('num_rows', models.PositiveSmallIntegerField(default=0)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Lesson')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.TypeGame')),
            ],
        ),
    ]
