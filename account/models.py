from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class AttendanceFile(models.Model):
#     id = models.AutoField(primary_key=True)
#     file = models.FileField(blank = True)
#     # or...


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    objects = models.Manager()

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    lecture_id = models.IntegerField(default = 0)
    session_start_time = models.DateTimeField()
    session_end_time = models.DateTimeField()
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING, default=1)
    file = models.FileField(null=True,blank=True, upload_to='documents/')
    objects = models.Manager()
    uploaded = models.BooleanField(default=False)


class User(AbstractUser):
    user_type_data = ((1, "Student"), (2, "Teacher"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    courses = models.ManyToManyField(Course)
    points = models.IntegerField(default = 100)
    attendance_percentage = models.PositiveIntegerField(default=0)
    number_of_class_attended = models.IntegerField(default = 0)
    

class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    points = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)


