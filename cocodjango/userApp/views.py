from django.shortcuts import render
from .models import Employee



def controlPanel(request):
    email = request.session.get('user_email')
    name = Employee.objects.get(email=email).name
    is_logged_in = True

    context = {
        "name": name,
        "email": email,
        "is_logged_in": is_logged_in
    }
    return render(request, 'userApp/controlPanel.html', context)