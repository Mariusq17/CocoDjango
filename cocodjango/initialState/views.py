from contextlib import nullcontext

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from userApp.models import Employee


# Create your views here.
def home(request):
    email = request.session.get('user_email')
    if email and Employee.objects.get(email=email).last_time_online is not None:
        return redirect(f'{reverse("controlPanel")}')
    return render(request, "initialState/landing.html", {})

def formMain(request):
    return render(request, "initialState/formPageMain.html")

from .models import Question, Answer

def form1(request):
    questions_with_answers = [
        (question, Answer.objects.filter(question_id=question.id))
        for question in Question.objects.all()
    ]

    context = {'questions_with_answers': questions_with_answers}
    return render(request, "initialState/formPage1.html", context)

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
    return render(request, "initialState/formPage2.html", context)

def form3(request):
    questions_with_answers = [
        (question, Answer.objects.filter(question_id=question.id))
        for question in Question.objects.all()
    ]

    context = {'questions_with_answers': questions_with_answers}
    return render(request, "initialState/formPage3.html", context)