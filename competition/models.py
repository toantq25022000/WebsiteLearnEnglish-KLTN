
from django.db import models
from django.conf import settings
from usermember.models import MyUser
from course.models import Course
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import json
from channels.layers import channel_layers, get_channel_layer
from asgiref.sync import async_to_sync
from django.db import transaction
# Create your models here.

class TypeCompetition(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150,default= '')
    max_quantity_add_user = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.title

class_choice = (
        (3,'Lớp 3'),
        (4,'Lớp 4'),
        (5,'Lớp 5'),
        (6,'Lớp 6'),
        (7,'Lớp 7'),
        (8,'Lớp 8')
    )

class RoomCompetition(models.Model):
    status_choice = (
        (0,'Phòng chờ'),
        (1,'Phòng riêng'),
        (2,'Đang thi'),
    )

    

    skill_choice = (
        ('Tổng hợp','Từ vựng - ngữ pháp - nghe & đọc hiểu'),
    )

    id_room = models.CharField(max_length=30,unique=True)
    user_host = models.ForeignKey(MyUser, on_delete = models.CASCADE, related_name='user_host')
    users = models.ManyToManyField(MyUser, blank = True, related_name='list_user', help_text='users who are connect to the competition')
    type_compete = models.ForeignKey(TypeCompetition, on_delete = models.CASCADE)
    class_compete = models.IntegerField(choices=class_choice, default = 3)
    skills = models.CharField(max_length=70,default = 'Tổng hợp',choices=skill_choice )
    is_private = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=status_choice, default = 0)


    class Meta:
        ordering = ['-create_date']


    def delete(self):
        room  = RoomCompetition.objects.filter(id = self.id)
        if len(room) > 0:
            room = room[0]
            channel_layers = get_channel_layer()
            item = {
                'id_room':room.id_room,
                'status_method_save':'delete',
            }
            data = []
            data.append(item)
            async_to_sync(channel_layers.group_send)(
                "competition_broadcast",
                {
                    'type':'send_change_or_create_room',
                    'message': list(data),
                })
                
        super(RoomCompetition, self).delete()
    
    def check_room_and_send_data(self,id_pk,method_save):
        room  = RoomCompetition.objects.filter(id = id_pk)
        if len(room) > 0:
            room = room[0]
            channel_layers = get_channel_layer()
           
            item = {
                'id':room.id,
                'id_room':room.id_room,
                'user_host': room.user_host.username,
                'img_user_host': room.user_host.std_img.url,
                'count_number_user': room.users.all().count() + 1,
                'count_max_user': room.type_compete.max_quantity_add_user,
                'type_compete': room.type_compete.title,
                'class_compete': room.class_compete,
                'skills': room.skills,
                'is_private': room.is_private,
                'status': room.get_status_display(),
                'status_method_save':method_save,
            }
            data = []
            data.append(item)
            async_to_sync(channel_layers.group_send)(
                "competition_broadcast",
                {
                    'type':'send_change_or_create_room',
                    'message': list(data),
                })
        return "Done"

    def save(self, *args, **kwargs):
        method_save = ''
        if self.id is None:
            method_save = 'create'
        else:
            method_save = 'update'
        self.update_date = timezone.localtime(timezone.now())
        super(RoomCompetition, self).save(*args, **kwargs)
       
        
        transaction.on_commit(lambda: self.check_room_and_send_data(self.id,method_save))
        

    def __str__(self):
        return f"Room of {self.user_host.username} - Id room: {self.id_room}"


class ListTopticCompetition(models.Model):
    title = models.CharField(default='',max_length=80)
    file_excel = models.FileField(upload_to='game/topic/', max_length=100)

    def __str__(self):
        return self.title

class TopicOfClassCompetition(models.Model):
    class_topic = models.IntegerField(choices=class_choice, default = 3)
    list_topic = models.ManyToManyField(ListTopticCompetition, blank = True, related_name='listTopic', help_text='')

    def __str__(self):
        return self.get_class_topic_display()

class ManagerCalculateRankingPoints(models.Model):
    rank1 = models.PositiveSmallIntegerField(default = 0)
    rank2 = models.PositiveSmallIntegerField(default = 0)
    rank3 = models.PositiveSmallIntegerField(default = 0)
    rank4_onwards = models.PositiveSmallIntegerField(default = 0)

    def __str__(self):
        return "Cách tính khi kết thúc xếp hạng điểm công thêm khi thi đấu"



class ManagerUserCompetition(models.Model):
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    title =  models.CharField(default='',max_length=75)
    star_title = models.PositiveSmallIntegerField(default=1)
    total_battle = models.PositiveSmallIntegerField(default=0)
    win_1v1 = models.PositiveSmallIntegerField(default=0)
    win_1v9 = models.PositiveSmallIntegerField(default=0)
    total_title = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.username
        
class ScoreCompetition(models.Model):
    
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    type_compete = models.ForeignKey(TypeCompetition, on_delete = models.CASCADE)
    result_rank = models.CharField(default='',max_length=75)
    points_title = models.PositiveSmallIntegerField(default=0)
    timestart =  models.DateTimeField()
    
    def __str__(self):
        return self.user.username




