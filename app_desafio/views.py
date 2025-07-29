from django.shortcuts import render

# Create your views here.


def empleados (request):
    categories = ["Pedro", "Juan", "Diego", "Cristian", "José"]
    context = {"categories": categories}
    return render(request, "empleados.html", context)
