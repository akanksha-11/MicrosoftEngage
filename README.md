Microsoft Engage Programme'21

Gamified digital learning 

Introduction

The aim of the project is to incentivise students to attend classes by rewarding them with points that they can redeem through coupons.
These coupons could be food or grocery coupons that can be given away by stores within university campus who are looking to market their products.

Tech Stack:

Backend : Django
Frontend : HTML, CSS, BOOTSTRAP
Database : MongoDB

The first thing to do is to clone the repository:

$ git clone https://github.com/akanksha-11/MicrosoftEngage.git
$ cd engage
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd engage
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/

For uploading attendance, choose nay file in /media/documents folder
Credentials:For students: Userid- student1 Password-engageone, student2, engagetwo and so on till student10
For teachers: Userid teacher1 Password- engageone and so on till teacher5



Features Implemented
1. Login by user type (teacher and student)
2. View courses of student/teacher
3. View all lectures of all courses for every teacher
4. Uploading attendance file for every lecture
5. Calculating attendance percentage for every student ( classes attended/ classes who's attendance has been uploaded)
6. Calculating course streak( which goes zero everytime a student doesn't attend a class)
7. Implemented a leaderboard of students based on attendance percentage
8. Rewarding points:
        1 point for attending a class
        4 points for attending 3 classes (3 classes per week)
        10 points for 2 weeks
        15 points for 3 weeks
        20 points for 1 month
   Greater number of points will override day wise points
9. Allowing students to redeeem a coupon only if they have enough points
10. Calculating attendance streak of all courses per student ( min(all course streaks))
11. Implementing notifications for every time you earn points

Assumptions/ Limitations
1. File should be uploaded only once for a particular course
2. Notification panel is not capped, will store all the notifications

Future work
1. Adding graphs by storing date wise attendance data as all sessions are mapped with dates as well but not used in this project as of now
2. Using Likes and Polls data in the attendance file to calculate engagement and reward points on that basis
3. Coupons can have validity feature as well






