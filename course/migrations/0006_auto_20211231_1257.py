# Generated by Django 3.0.14 on 2021-12-31 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20211230_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamegoldenfish',
            name='file_excel',
            field=models.FileField(upload_to='game/golden_fish/'),
        ),
        migrations.AlterField(
            model_name='imageofgame',
            name='img',
            field=models.ImageField(upload_to='game/memory_word_card/'),
        ),
    ]
