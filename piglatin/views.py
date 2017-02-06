from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def translate(request):
    newtext = request.GET['sss'].lower()
    translation = ''
    for word in newtext.split():
        if word[0] in ['a','e','i','o','u']:
            translation += word
            translation += 'yay '
        else:
            translation += word[1:]
            translation += word[0]
            translation += 'ay '
    return render(request,'translate.html',{'origtext':newtext,'trans':translation})
def about(request):
    return render(request,'about.html')
