# Generated by Django 3.0.14 on 2021-12-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0005_roomcompetition_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomcompetition',
            options={'ordering': ['-create_date']},
        ),
        migrations.AddField(
            model_name='roomcompetition',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
