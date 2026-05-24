from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse

# Create your views here.
def home(request):
    # query = request.GET.get('search')
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees}) 

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def details(request, id):
    employee = Employee.objects.get(id=id)
    context = {
        'employee' : employee,
    }
    return render(request, 'details.html',context)

def update(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.eid = request.POST.get('eid')
        employee.salary = request.POST.get('salary')
        employee.position = request.POST.get('position')
        
        employee.save()

        return redirect('home')
    
    context = {
        'employee': employee,
    }
    return render(request, 'update.html', context)
    
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        eid = request.POST.get('eid')
        salary = request.POST.get('salary')
        position = request.POST.get('position')
        
        try:
            Employee.objects.create(name=name, eid=eid, salary=salary, position=position)
        except:
            return HttpResponse('Not Found')
        
        return redirect('home')
    
    return render(request, 'create.html')

def delete(request,id):
    employee = Employee.objects.get(id=id)
    
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    
    context = {
        'employee' : employee,
    }
    
    return render(request, 'delete.html', context)