import requests
from django.core.management.base import BaseCommand
from quiz_app.models import Question

class Command(BaseCommand):
    help = 'Load quiz questions from Open Trivia Database into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--difficulty',
            type=str,
            choices=['easy', 'medium', 'hard'],
            default='medium',
            help='Difficulty level of the questions to load (easy, medium, hard)'
        )

    def handle(self, *args, **options):
        difficulty = options['difficulty']
        url = f'https://opentdb.com/api.php?amount=15&type=multiple&difficulty={difficulty}'
        response = requests.get(url)
        data = response.json()

        if data['response_code'] == 0:
            for item in data['results']:
                question_text = item['question']
                options = item['incorrect_answers']
                options.append(item['correct_answer'])
                options.sort()
                correct_option = chr(65 + options.index(item['correct_answer']))  # 'A', 'B', 'C', 'D'
                difficulty = item['difficulty']

                Question.objects.create(
                    question_text=question_text,
                    option_a=options[0],
                    option_b=options[1],
                    option_c=options[2],
                    option_d=options[3],
                    correct_option=correct_option,
                    difficulty=difficulty
                )

            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {difficulty} questions from OpenTDB'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch questions from OpenTDB'))