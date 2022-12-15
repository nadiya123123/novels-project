from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import new
from .forms import novelform

# Create your views here.

def fun1(request):
    x=new.objects.all()
    y={
        'novels':x
    }
    return render(request,"index.html",y)
def details(request,x_id):
    x = new.objects.get(id=x_id)
    return render(request,"details.html",{'novel': x})
def add_novels(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        year= request.POST.get('year', )
        desc= request.POST.get('desc', )
        img= request.FILES['img']
        novels=new(name=name,year=year,desc=desc,img=img)
        novels.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    novel=new.objects.get(id=id)
    form=novelform(request.POST or None,request.FILES,instance=novel)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'novel':novel})
def delete(request,id):
    if request.method == 'POST':
        novel=new.objects.get(id=id)
        novel.delete()
        return redirect('/')
    return render(request, 'delete.html')