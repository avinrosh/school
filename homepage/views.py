from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict={'insert_me':"Welcome to Kidz Central!!!!"}
    return render(request,'homepage/index.html',context=my_dict)
