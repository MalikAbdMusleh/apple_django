from django.urls import path
from . import views
urlpatterns=[
path("",views.types,name="types")
]
