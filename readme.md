# Quiz App

This is a Django-based Quiz Application that allows users to take quizzes with questions fetched from a local database. The application supports different difficulty levels and provides a summary of the quiz results.

## Features

- Start a quiz with a specified number of questions and difficulty level.
- Answer questions one by one with options to navigate between questions.
- Submit answers and view quiz results with statistics.
- Load sample questions from the Open Trivia Database into the local database.

## Prerequisites

- Python 3.8+
- PostgreSQL
- Virtual environment tool (e.g., `venv` or `virtualenv`)

## Setup

1. **Clone the repository:**

```sh
git clone https://github.com/JeyasuryaUR/QuizApp
cd QuizApp
```

2. **Create and activate a virtual environment:**

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the dependencies:**

```sh
pip install -r requirements.txt
```

4. **Set up the environment variables:**

Create a `.env` file in the root directory and add the following variables:

```
SECRET_KEY=your_secret_key  # Optional
DEBUG=True  # Optional
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host 
DB_PORT=your_db_port
```

5. **Run database migrations:**

```sh
python manage.py migrate
```

6. **Load sample questions into the database:**

You can load sample questions from the Open Trivia Database using the following commands:

```sh
python manage.py load_sample_questions --difficulty easy
python manage.py load_sample_questions --difficulty medium
python manage.py load_sample_questions --difficulty hard
```

These commands will fetch questions from the Open Trivia Database (https://opentdb.com/) and load them into your local database.

7. **Run the development server:**

```sh
python manage.py runserver
```

8. **Access the application:**

Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Start a Quiz:**

   - Go to the home page.
   - Enter the number of questions and select the difficulty level.
   - Click on the "Start Quiz" button.

2. **Answer Questions:**

   - Navigate through the questions using the "Previous" and "Next" buttons.
   - Select an answer for each question.

3. **Submit Answers:**

   - After answering all questions, click on the "Submit" button.
   - View the quiz results with statistics.

## Project Structure

- client: Contains the client-side code including templates and views.
- quiz_app: Contains the main application logic including models, serializers, views, and management commands.
- quiz_project: Contains the project settings and URLs.
- requirements.txt: List of project dependencies.
- build.sh: Shell script for setting up the project.

## Deployment

To deploy the application, you can use services like Heroku, Render, or any other cloud provider that supports Django applications. Make sure to configure the environment variables and database settings accordingly.

## Contact

For any questions or inquiries, please contact [jeyasurya0206@example.com].
