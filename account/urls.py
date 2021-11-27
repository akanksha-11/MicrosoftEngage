from django.urls import path

from engage.settings import MEDIA_URL
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
   
    path('student/<student_id>/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('schedule/', views.schedule, name='schedule'),
    path('course/<course_id>/', views.view_course, name="viewcourse"),
    path('session/<session_id>/', views.view_session, name="viewsession"),
    path('coupon/<user_id>/<coupon_id>/', views.collect, name="collect"),  
    path('rewards/', views.rewards, name='rewards'),


    

   
]
if(settings.DEBUG):
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)