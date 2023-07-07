from django.http.response import HttpResponse
from django.shortcuts import render


def HelloWorld(request):
    context = {
            "title": "Softlixx",
            "color": "greenasd",
            "fruits": ['Apple', 'Mango', 'Cherry', 'Peach'],
            "student": {"name": "Ahmad", "age": "26"}
        }
    return render(request, 'index.html', context)


def students(request):
    aaa = [
        {"id": 1, "name": "John", "age": 24},
        {"id": 2, "name": "Smith", "age": 32},
        {"id": 3, "name": "Will", "age": 72},
        {"id": 4, "name": "Mosh", "age": 82},
        {"id": 5, "name": "Chris", "age": 92},
        {"id": 6, "name": "Robert", "age": 92},
    ]
    return render(request, 'students.html', {"students": aaa})