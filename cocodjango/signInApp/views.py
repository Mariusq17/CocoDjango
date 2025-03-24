from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from .forms import RawSignInForm
from userApp.models import Employee

def formPage(request):
    # Varianta improvizata: cand intri pe login se sterge sesiunea
    request.session.flush()
    my_form = RawSignInForm()

    if request.method == "POST":
        my_form = RawSignInForm(request.POST)

        if my_form.is_valid():
            email = my_form.cleaned_data['email']
            password = my_form.cleaned_data['password']

            user = Employee.objects.filter(email=email).first()  # Evită eroarea de obiect inexistent
            if user and password == user.password:
                request.session['user_email'] = email
                return redirect(f'{reverse("controlPanel")}')
            else:
                print("Email sau parolă incorectă")
    context = {
        'form': my_form
    }
    return render(request, "signInApp/signInPage.html", context)