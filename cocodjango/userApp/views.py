from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
        return redirect("formPage")
    context = {"name": name, 'user': user}
    return render(request, 'userApp/controlPanel.html', context)

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