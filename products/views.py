from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def HelloWorld(request):
    return render(request, 'index.html')
    # text = "Some thing Some thing"
    # return HttpResponse(f'<h1>{text}</h1>')