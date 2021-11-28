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

$ git clone https://github.com/
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

