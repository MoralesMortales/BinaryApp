from django.shortcuts import render
from .mainCode import binaryConverterCode
# Create your views here

def mainPage(request):
    result = None
    if request.method == 'POST':
        number = int(request.POST.get('numberSender'))
        result = binaryConverterCode(number) 
    return render(request, 'index.html' , {'result': result})
