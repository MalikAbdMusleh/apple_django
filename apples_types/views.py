from django.shortcuts import render
from .models import Apples
# Create your views here.
def types(request):
    get_all_data=Apples.objects.all()
    data={
    "get_all_data":get_all_data
    }
    return render(request,"apple_photos.html",data)
