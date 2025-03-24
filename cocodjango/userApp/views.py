from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.

from .models import Employee
def controlPanel(request):
    email = request.session.get('user_email')
    name = Employee.objects.get(email=email).name
    context = {"name": name}
    return render(request, 'userApp/controlPanel.html', context)