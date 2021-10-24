from django.urls import path
from . import views
urlpatterns=[
path("",views.types,name="types"),
path('delete/<int:id>', views.destroy),
path('create/', views.create,name="create"),
path('update/<int:id>', views.update,name="update"),

]
