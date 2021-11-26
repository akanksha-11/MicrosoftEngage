from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.db.models import OuterRef, Subquery
import datetime
import csv
import pandas as pd
import io
from io import StringIO


from account.models import Coupon, Course, Session, User
from .forms import DocumentForm, LoginForm
# from account.forms import AttendanceForm
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, 'index.html')


# def register(request):
#     msg = None
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             msg = 'user created'
#             return redirect('login_view')
#         else:
#             msg = 'form is not valid'
#     else:
#         form = SignUpForm()
#     return render(request,'register.html', {'form': form, 'msg': msg})


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
    students = User.objects.filter(user_type="1")
    students = students.order_by('-attendance_percentage')
    
    start_date = datetime.date(2020,1,1)
    end_date = datetime.date(2020,5,4)
    delta = datetime.timedelta(days=1)
    
    while start_date <= end_date:
        if(start_date=="2020-04-25"):
            print(start_date)
            start_date += delta
    rank = student_id
    context = {
        "students": students,
        "attendance_rank": rank
        # "attendance_percentage": percentage
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


def view_session(request, session_id):
    session = Session.objects.get(id=session_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=session)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    else:
        form = DocumentForm()
    df = pd.read_csv(io.StringIO(session.file.read().decode('utf-8')), delimiter=',')
    for index, row in df.iterrows():
        user = User.objects.get(id = row['Student ID'])
        if row['Duration']>=40 :
            user.number_of_class_attended+=1
            user.save()

    


    return render(request, 'session_teacher.html', {
        'form': form,
        'session':session 
    })


def collect(request, user_id,coupon_id):
    coupon = Coupon.objects.get(id=coupon_id)
    user = User.objects.get(id=user_id)
    ans = "You don't have enough points"
    if user.points>=coupon.points :
        user.points = user.points - coupon.points
        ans = "Redeemed"

    User.objects.filter(id=user_id).update(points=user.points)
    context = {
        "ans": ans,
        "user_id": user_id,
        "coupon_points": coupon.points,
        "coupon_desc": coupon.description
    }
    
    return render(request,'coupon.html',context)
    

  
def rewards(request):
    coupons = Coupon.objects.all()
    context = {
        "coupons": coupons
    }
    return render(request,'rewards.html',context)  