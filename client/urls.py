from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/<int:session_id>/', views.quiz_session, name='quiz_session'),
    path('quiz/<int:session_id>/result/', views.quiz_result, name='quiz_result'),
]