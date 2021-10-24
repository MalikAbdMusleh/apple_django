from django.shortcuts import render,redirect
from .models import Apples
from .forms import AddApple
# Create your views here.
def types(request):
    get_all_data=Apples.objects.all()
    data={
    "get_all_data":get_all_data
    }
    return render(request,"apple_photos.html",data)

def destroy(request, id):
    Apple = Apples.objects.get(id=id)
    Apple.delete()
    return redirect("/types")

# def update(request, id):
#     employee = Apples.objects.get(id=id)
#     form = EmployeeForm(request.POST, instance = employee)
#     if form.is_valid():
#         form.save()
#         return redirect("/show")
#     return render(request, 'edit.html', {'employee': employee})

def create(request):
    form=AddApple()
    if request.method=="POST":
        form=AddApple(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/types")
    data={
    "form":form
    }
    return  render(request,"create.html",data)

def update(request,id):
    apple =Apples.objects.get(id=id)
    form=AddApple(instance=apple)
    if request.method=="POST":
        form=AddApple(request.POST,instance=apple) # to replace the instance row with the new field without add new new row
    if form.is_valid():
        form.save()
        return redirect("/types")
    data={"form":form}
    return  render(request,"create.html",data)
