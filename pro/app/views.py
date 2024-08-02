from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .forms import UserForm

# Create your views here.

def add(request):
    stu = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
    else:
        form = UserForm()        
    
    return render(request, 'add.html',{'form':form,'stud':stu})
def delete(request,id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        user.delete()
        return HttpResponseRedirect('/')
    
    
def update(request,id):
    if request.method == 'POST':
        p = User.objects.get(pk=id)
        form = UserForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            form = UserForm()
    else:
        p = User.objects.get(pk=id)
        form = UserForm(instance=p)        
    return render(request, 'update.html', {'form': form})        