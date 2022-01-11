from django.db import models

# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(default='',max_length=55)
    email = models.EmailField(max_length=55)
    phone = models.CharField(default='',max_length=11)
    address = models.TextField(default='',max_length=255)
    content = models.TextField(default='',max_length=255)
    time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.id}. {self.fullname}"
    
