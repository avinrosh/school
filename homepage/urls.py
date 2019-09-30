from django.conf.urls import url
from django.urls import path
from homepage import views

urlpatterns= [

    path("",views.IndexView.as_view(),name='index'),
    path("<int:parent_id>/homepage/",views.details,name='details'),
]
