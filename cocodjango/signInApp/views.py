from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .forms import RawSignInForm
from userApp.models import Employee

def formPage(request):
    # Varianta improvizata: cand intri pe login se sterge sesiunea
    # request.session.flush()
    my_form = RawSignInForm()

    if request.method == "POST":
        my_form = RawSignInForm(request.POST)

        if my_form.is_valid():
            email = my_form.cleaned_data['email']
            password = my_form.cleaned_data['password']

            user = Employee.objects.filter(email=email).first()  # Evită eroarea de obiect inexistent
            if user and password == user.password:
                request.session['user_email'] = email
                if user.last_time_online is None:
                    return redirect('resetPassword')
                
                return redirect(f'{reverse("controlPanel")}')
            else:
                print("Email sau parolă incorectă")
    context = {
        'form': my_form
    }
    return render(request, "signInApp/signInPage.html", context)

@csrf_exempt
def update_last_online(request):
    """Actualizează last_time_online la ieșirea utilizatorului"""
    user_email = request.session.get('user_email')

    if not user_email:  # Dacă sesiunea nu există, nu face nimic
        return JsonResponse({"status": "session expired"}, status=403)

    try:
        user = Employee.objects.get(email=user_email)
        user.last_time_online = datetime.datetime.now()
        user.save()
        return JsonResponse({"status": "success"})
    except Employee.DoesNotExist:
        return JsonResponse({"status": "error"}, status=404)

from .forms import ResetPasswordForm
import datetime
def resetPasswordFormPage(request):
    email = request.session.get('user_email')
    if not email:
        return redirect("home")
    
    user = Employee.objects.get(email=email)
    my_form = ResetPasswordForm()

    if request.method == "POST":
        my_form = ResetPasswordForm(request.POST)
        if my_form.is_valid():
            password = my_form.cleaned_data['password']
            confirm_password = my_form.cleaned_data['confirm_password']
            if password != confirm_password:
                print("Parolele nu se potrivesc")
            else:
                print("Parola salvata!")
                user.password = password
                user.last_time_online = datetime.datetime.now()
                user.save()
                return redirect("controlPanel")
            
    context = {
        'form': my_form
    }
    return render(request, "signInApp/resetPassword.html", context)