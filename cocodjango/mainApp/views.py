from contextlib import nullcontext

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("HelloWorld")

def formMain(request):
    return render(request, "mainApp/formPageMain.html")

from .models import Question, Answer

def form1(request):
    questions_with_answers = [
        (question, Answer.objects.filter(question_id=question.id))
        for question in Question.objects.all()
    ]

    context = {'questions_with_answers': questions_with_answers}
    return render(request, "mainApp/formPage1.html", context)

def form2(request):
    questions_with_answers = [
        (question, Answer.objects.filter(question_id=question.id))
        for question in Question.objects.all()
    ]
    posted_data = None
    if request.method == 'POST':
        posted_data = request.POST.get('3').strip()

    context = {
        'questions_with_answers': questions_with_answers,
        'posted': posted_data,
    }
    return render(request, "mainApp/formPage2.html", context)

def form3(request):
    questions_with_answers = [
        (question, Answer.objects.filter(question_id=question.id))
        for question in Question.objects.all()
    ]

    context = {'questions_with_answers': questions_with_answers}
    return render(request, "mainApp/formPage3.html", context)