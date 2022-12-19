from django.db import models

# Create your models here.


class Partner(models.Model):
    name = models.CharField(max_length=100)
    creation_timestamp = models.DateTimeField()
    last_update_timestamp = models.DateTimeField()
    user_update = models.CharField(max_length=100)
    
class Mail(models.Model):
    name = models.CharField(max_length=100)
    is_subscribe = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    creation_timestamp = models.DateTimeField()
    last_update_timestamp = models.DateTimeField()
    
class Mail_Partner(models.Model):
    id_mail = models.ForeignKey(Mail,on_delete=models.CASCADE)
    id_partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    creation_timestamp = models.DateTimeField()
    last_update_timestamp = models.DateTimeField()
class Message(models.Model):
    id_mail = models.ForeignKey(Mail,on_delete=models.CASCADE)
    content = models.TextField()
    sent_timestamp = models.DateTimeField()
