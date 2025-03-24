from django.shortcuts import render, redirect

# Create your views here.

from .models import Employee
import datetime
def controlPanel(request):
    email = request.session.get('user_email')

    if not email:
        return redirect("home")

    name = Employee.objects.get(email=email).name
    user = Employee.objects.get(email=email)
    if request.method == "POST":
        user.last_time_online = datetime.datetime.now()
        user.save()
        request.session.flush()
        return redirect("home")
    context = {"name": name, 'user': user}
    return render(request, 'userApp/controlPanel.html', context)

