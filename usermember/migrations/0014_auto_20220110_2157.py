# Generated by Django 3.0.14 on 2022-01-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermember', '0013_auto_20220110_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='std_img',
            field=models.ImageField(default='https://www.dungplus.com/wp-content/uploads/2019/12/girl-xinh-1-480x600.jpg', upload_to='user/image-student/'),
        ),
    ]
