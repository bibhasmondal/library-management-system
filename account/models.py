from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date
from datetime import datetime
import base64
# Create your models here.

class Student(models.Model):
    DEPT_CHOICES = (('ME', 'Mechanical Engineering'),
        ('CSE', 'Computer Science and Engineering'),
        ('EE', 'Electrical Engineering'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics and Communications'),
        ('MCA', 'Master of Computer Application'),
        ('MME', 'MTech: Mechanical'),
        ('MCSE', 'MTech: Computer Science'),
        ('MIT', 'MTech: Information Technology'),
        ('MEE', 'MTech: Electrical Engineering'),
        ('MECE', 'MTech: Electronics and Communication'),
        )

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    dp = models.TextField(blank=True, default=base64.encodestring(open('media/account/default.png', 'rb').read()).decode('utf-8'))
    Name = models.CharField(max_length = 50)
    Year_Of_Passing = models.DecimalField(max_digits = 4, decimal_places = 0)
    Department = models.CharField(choices = DEPT_CHOICES, max_length=40)
    Address=models.TextField(blank=True)
    Mobile_No=models.DecimalField(max_digits=14,decimal_places=0,blank=True,null=True)
    def __str__(self):
        return self.Name
