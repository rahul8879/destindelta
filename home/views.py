from django.shortcuts import render

# Create your views here.


def home(request):
    ''' This function will return the home page content'''
    return render(request, 'pages/home.html')
