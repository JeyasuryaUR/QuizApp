from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question, QuizSession
from .serializers import QuestionSerializer, QuizSessionSerializer
import random
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def start_quiz(request):
    try:
        amount = int(request.GET.get('amount', 5))
        difficulty = request.GET.get('difficulty', 'medium')
        questions = list(Question.objects.filter(difficulty=difficulty))
        if len(questions) < amount:
            return Response({"message": "Not enough questions available"}, status=400)

        selected_questions = random.sample(questions, amount)
        question_ids = [q.id for q in selected_questions]

        session = QuizSession.objects.create(
            total_questions=amount,
            difficulty=difficulty,
            question_ids=question_ids
        )

        return Response({
            "message": "Quiz started",
            "session_id": session.id,
            "questions": QuestionSerializer(selected_questions, many=True).data
        })
    except Exception as e:
        logger.error(f"Error starting quiz: {e}")
        return Response({"message": "Internal server error"}, status=500)

@api_view(['POST'])
def submit_answers(request):
    session_id = request.data.get('session_id')
    answers = request.data.get('answers', [])

    session = QuizSession.objects.get(id=session_id)
    correct_count = 0
    incorrect_count = 0

    for answer in answers:
        question_id = answer['question_id']
        selected_option = answer['selected_option'].upper()

        question = Question.objects.get(id=question_id)
        if selected_option == question.correct_option:
            correct_count += 1
        else:
            incorrect_count += 1

    session.correct_count = correct_count
    session.incorrect_count = incorrect_count
    session.save()

    return Response({
        "total_attempts": correct_count + incorrect_count,
        "correct": correct_count,
        "incorrect": incorrect_count
    })

@api_view(['GET'])
def get_stats(request):
    session_id = request.GET.get('session_id')
    session = QuizSession.objects.get(id=session_id)
    serializer = QuizSessionSerializer(session)

    return Response(serializer.data)

@api_view(['GET'])
def get_questions(request):
    try:
        session_id = request.GET.get('session_id')
        session = QuizSession.objects.get(id=session_id)
        question_ids = session.question_ids
        questions = Question.objects.filter(id__in=question_ids)
        return Response(QuestionSerializer(questions, many=True).data)
    except QuizSession.DoesNotExist:
        return Response({"message": "Quiz session not found"}, status=404)
    except Exception as e:
        logger.error(f"Error fetching questions: {e}")
        return Response({"message": "Internal server error"}, status=500)