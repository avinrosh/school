from django.shortcuts import render
from django.http import HttpResponse
from .models import Parent, Child

# Create your views here.
def index(request):
    parent_list=Parent.objects.all()
    parent_context={'parent_list':parent_list}
    return render(request,'homepage/index.html',parent_context)

def details(request,parent_id):
    child_details= Parent.objects.get(pk=parent_id)
    child_context={'child_details':child_details}
    return render(request,'homepage/details.html',child_context)
