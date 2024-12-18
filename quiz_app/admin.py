from django.contrib import admin

# Register your models here.
from .models import Question, QuizSession

admin.site.register(Question)
admin.site.register(QuizSession)