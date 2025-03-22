from django.shortcuts import render

# Create your views here.
def formPage(request):
    context = {}
    return render(request, "signInApp/signInPage.html", context)