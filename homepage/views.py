from django.shortcuts import render
from django.http import HttpResponse
from .models import Parent, Child
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name='homepage/index.html'
    context_object_name='parent_list'

    def get_queryset(self):
        return Parent.objects.all()

def details(request,parent_id):
    child_details= Parent.objects.get(pk=parent_id)
    child_context={'child_details':child_details}
    return render(request,'homepage/details.html',child_context)
