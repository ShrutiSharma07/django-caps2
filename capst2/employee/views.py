from django.shortcuts import render, redirect

# Create your views here.
from .models import Employee
from .forms import EmployeeForm


def all_employees(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'emp/index.html', context)


from django.contrib import messages


def add_employees(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"Employee {form.cleaned_data.get('name')} named employee has been added")
        return redirect('all_Employees')

    context = {
        'form': form,
    }
    return render(request, 'emp/EmployeeAdd.html', context)


def edit_employees(request, id=None):
    one_emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=one_emp)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('name')} named employee has been updated")
        return redirect('all_Employees')

    context = {
        'form': form,
    }
    return render(request, 'emp/EmployeeEdit.html', context)


def one_employee(request, id=None):
    emp = Employee.objects.get(id=id)
    context = {
        'emp': emp
    }
    return render(request, 'emp/EmployeeView.html', context)


def delete_employee(request, id=None):
    emp = Employee.objects.get(id=id)
    if request.method == "POST":
        emp.delete()
        messages.add_message(request, messages.INFO, f"{emp.name} named employee has been deleted")
        return redirect('all_Employees')
    context = {
        'emp': emp
    }
    return render(request, 'emp/EmployeeDelete.html', context)


def home_view(request):
    context = dict()
    return render(request, 'emp/home.html', context)
