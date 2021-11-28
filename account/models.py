from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from djongo import models
from django.contrib.postgres.fields import ArrayField

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
    session_date = models.DateField()
    session_hour = models.IntegerField(default=1)
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING, default=1)
    file = models.FileField(null=True,blank=True, upload_to='documents/')
    uploaded = models.IntegerField(default = 0)
    objects = models.Manager()


# class Notifications(models.Model):
#     id = models.AutoField(primary_key=True)
#     # messages = ArrayField(ArrayField(models.CharField(max_length=255),size = 6))
#     objects = models.Manager()

class User(AbstractUser):
    user_type_data = ((1, "Student"), (2, "Teacher"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    courses = models.ManyToManyField(Course, through='Enrollment')
    points = models.IntegerField(default = 0)
    attendance_percentage = models.PositiveIntegerField(default=0)
    number_of_class_attended = models.IntegerField(default = 0)
    streak = models.IntegerField(default = 0)
    messages = models.TextField(default="Welcome")

    

 
class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_streak = models.IntegerField(default=0)
    
    

class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    points = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)


