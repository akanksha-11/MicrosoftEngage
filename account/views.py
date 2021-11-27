from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.db.models import OuterRef, Subquery
from django.db.models import Count, F, Value
import datetime
import csv
import pandas as pd
import io
from io import StringIO


from account.models import Coupon, Course, Enrollment, Session, User
from .forms import DocumentForm, LoginForm
# from account.forms import AttendanceForm
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, 'index.html')



def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            user_type = user.user_type
            
            if user is not None and user_type == '1':
                login(request, user)
                return redirect('student',user.id)
                
            elif user is not None and user_type == '2':
               login(request, user)
               return redirect('teacher')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


    
    


def student(request, student_id):
    coupons = Coupon.objects.all()
    context = {
        "coupons": coupons
    }
    rank = 0
    user = User.objects.get(id=student_id)
    students = User.objects.filter(user_type="1").order_by('-attendance_percentage')
    for x in students:
        if x.attendance_percentage > user.attendance_percentage:
            rank+=1
    
    rank+=1
    e = Enrollment.objects.filter(user_id=student_id).values_list('course_streak')
    min = e.order_by('course_streak').first()
    streak = min[0]
    percentage = 0
    total_classes  = 0
    for x in Course.objects.filter(user = student_id):
             total_classes +=Session.objects.filter(course=x,uploaded =1).count()
    if total_classes!=0:
        percentage = (user.number_of_class_attended / total_classes)*100
        user.attendance_percentage = percentage
        user.save()

    # rank = student_id
    # rank = User.objects.filter(user_type="1",id = student_id).order_by('-attendance_percentage').count()
    # rank = students.filter(id = student_id).count()
    
    context = {
        "students": students,
        "attendance_rank": rank,
        "streak":streak,
        "attendance_percentage": percentage,
        "course_streak":e
    }
    return render(request,'student.html',context)

def teacher(request):
    return render(request,'teacher.html')


def schedule(request):
    return render(request,'schedule.html')

def view_course(request, course_id):
    course = Course.objects.get(id=course_id)
    
    context = {
        "course": course,
        "id": course_id
    }
    
    return render(request, 'course_teacher.html', context)


def view_session(request,session_id):
    session = Session.objects.get(id=session_id)
    courseid = session.course.id
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=session)
        if form.is_valid():
            form.save()
            Session.objects.filter(id=session_id).update(uploaded=1)        
            return redirect('viewcourse',courseid)
    else:
        form = DocumentForm()
    
    if session.file:
        df = pd.read_csv(io.StringIO(session.file.read().decode('utf-8')), delimiter=',')
        for index, row in df.iterrows():
            user = User.objects.get(id = row['Student ID'])
            if row['Duration']>=40 :
                user.number_of_class_attended+=1
                p = 0
                e = Enrollment.objects.get(course_id =courseid,user_id= user.id).course_streak+1
                if e==12 :
                    p=20
                elif e==9:
                    p=15
                elif e==6:
                    p=10
                elif e==3:
                    p=4
                else:
                    p=1
                user.points+=p
                user.save()
                # notification = "You just earned"+p+"points for attending Lecture"+ session_id+"of Course"+session.course.course_name
                
                Enrollment.objects.filter(course_id =courseid,user_id= user.id).update(course_streak = e)             
            
            else:
                Enrollment.objects.filter(course_id =courseid,user_id= user.id).update(course_streak = 0) 
                
    
    return render(request, 'session_teacher.html', {
        'form': form,
        'session':session
    })
    


def collect(request, user_id,coupon_id):
    coupon = Coupon.objects.get(id=coupon_id)
    user = User.objects.get(id=user_id)
    ans = 0
    if user.points>=coupon.points :
        user.points = user.points - coupon.points
        ans = 1

    User.objects.filter(id=user_id).update(points=user.points)
    context = {
        "ans": ans,
        "user_id": user_id,
        "coupon": coupon
    }
    
    return render(request,'coupon.html',context)
    

  
def rewards(request):
    coupons = Coupon.objects.all()
    context = {
        "coupons": coupons
    }
    return render(request,'rewards.html',context)  