# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from student.models import problems
from django.utils import timezone
# Create your models here.
class technician(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.BigIntegerField(default=0)
    problems_count = models.IntegerField()
    
    def __str__(self):
        return self.username
class admin_notify(models.Model):   
    tech = models.ForeignKey(technician, on_delete=models.CASCADE)
    notify =  models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.tech.username 
        
class notifications(models.Model):
    stu1 = models.ForeignKey(problems, on_delete=models.CASCADE,blank=True,null=True)
    problem_type = models.CharField(max_length=30)
    slot = models.DateField(null=True, default=None)
    data = models.CharField(max_length=40,default="added")
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.stu1.stu.id_no

class reports(models.Model):
    no_of_students = models.IntegerField()
    class_room = models.CharField(max_length=4)
    dept = models.CharField(max_length=30)
    block = models.CharField(max_length=30)
    amplifier = models.CharField(max_length=30)
    speakers = models.CharField(max_length=30)
    audio_port = models.CharField(max_length=30)
    audio_cable  = models.CharField(max_length=30)
    projector = models.CharField(max_length=30)
    screen = models.CharField(max_length=30)
    video_cable = models.CharField(max_length=30)
    vga_port = models.CharField(max_length=30)
    io_port_not_working_positions = models.CharField(max_length=150)
    how_many_lan_cables_not_working = models.CharField(max_length=150) 
    issued_lan_cables = models.IntegerField()
    class_room_ip = models.GenericIPAddressField()
    switch = models.CharField(max_length=30)
    rack = models.CharField(max_length=30)
    adapters_not_working = models.CharField(max_length=150)
    adapters_working = models.CharField(max_length=150)
    screen_damage = models.CharField(max_length=50)
    d_link_modem = models.CharField(max_length=30)
    jio_modem = models.CharField(max_length=30)
    bio_metric_essl_not_registered = models.CharField(max_length=200)
    bio_metric_aadhar_not_registered = models.CharField(max_length=200)
    bio_metric_problems_if_any = models.CharField(max_length=200)
    
    def __str__(self):
        return self.class_room
   
            
                    
