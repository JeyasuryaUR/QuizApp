from django.urls import path
from . import views

urlpatterns = [
    path("quiz/start/", views.start_quiz, name="start_quiz"),
    path("quiz/submit/", views.submit_answers, name="submit_answer"),
    path("quiz/stats/", views.get_stats, name="get_stats"),
    path("quiz/questions/", views.get_questions, name="get_questions"),
]