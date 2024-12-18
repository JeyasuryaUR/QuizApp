from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # 'A', 'B', 'C', 'D'
    difficulty = models.CharField(max_length=10, default="medium")  # 'easy', 'medium', 'hard'

    def __str__(self):
        return self.question_text

class QuizSession(models.Model):
    user_id = models.CharField(max_length=50, default="guest_user")
    question_ids = models.JSONField(default=list)
    total_questions = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=10, default="medium")
    correct_count = models.IntegerField(default=0)
    incorrect_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)