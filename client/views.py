from django.shortcuts import render

def index(request):
    return render(request, 'client/index.html')

def quiz_session(request, session_id):
    return render(request, 'client/quiz_session.html', {'session_id': session_id})

def quiz_result(request, session_id):
    return render(request, 'client/quiz_result.html', {'session_id': session_id})
