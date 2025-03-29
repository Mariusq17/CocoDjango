from django.shortcuts import render
from .models import Employee

def controlPanel(request):
    email = request.session.get('user_email')
    user = Employee.objects.get(email=email)
    is_logged_in = True

    users = Employee.objects.all()

    suma = 0
    for user in users:
        suma += user.salary

    context = {
        "user": user,
        "users": users,
        "numOfEmployees": len(users),
        "suma": suma,
        "email": email,
        "is_logged_in": is_logged_in
    }
    return render(request, 'userApp/controlPanel.html', context)

from .forms import UpdateProfileForm
def viewProfile(request):
    user = Employee.objects.get(email=request.session.get('user_email'))
    form = UpdateProfileForm(initial={
        'name': user.name,
        'email': user.email,
        'password': '',  # Parola nu se pre-populează din motive de securitate
        'available': user.available,
        'start_date': user.start_date,
        'position': user.position,
        'my_buddy': user.my_buddy
    })
    context = {'form': form}
    return render(request, 'userApp/viewProfile.html', context)


