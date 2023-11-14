from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from . app_forms import EmployeeForm, LoginForm
from . models import Employee
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

@login_required
@permission_required('mainapp.add_employee', raise_exception=True)
def index(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Employee was added succesfully")
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'employee.html', {"form":form})

@login_required
def all_employees(request):
    employees = Employee.objects.all()  # SELECT * FROM employees
    # employees = Employee.objects.all().order_by("-salary")
    # employees = Employee.objects.filter(name__istartswith="La").order_by("dob")
    # employees = Employee.objects.filter(name__istartswith="La", salary__gt=45000).order_by("dob")
    # employees = Employee.objects.filter(Q(name__contains="la") | Q(salary__gt=70000))
    # employees = Employee.objects.filter(Q(name__contains="la") & Q(salary__gt=70000))
    # employees = Employee.objects.filter(Q(name__contains="la") & ~Q(salary__gt=70000)) # tilde
    # today = datetime.today()
    # day = today.day
    # month = today.month
    # employees = Employee.objects.filter(dob__day=day, dob__month=month)  # tilde
    paginator = Paginator(employees, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, "all_employees.html", {"employees": data})

@login_required
def employee_details(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)
    return render(request, 'employee_details.html', {"employee":employee})

@login_required
@permission_required('mainapp.delete_employee', raise_exception=True)
def employee_delete(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    employee.delete()
    messages.success(request, "Employee was deleted permanently")
    return redirect("all")

@login_required
@permission_required('mainapp.view_employee', raise_exception=True)
def search_employees(request):
    search_word = request.GET["search_word"]
    employees = Employee.objects.filter(
        Q(name__icontains=search_word) | Q(email__icontains=search_word)
    )
    paginator = Paginator(employees, 20)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    # Elastic search
    return render(request, "all_employees.html", {"employees": data})

@login_required
@permission_required('mainapp.change_employee', raise_exception=True)
def employee_update(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee was updated succesfully")
            return redirect('details', emp_id)
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'update.html', {"form":form})

def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
        messages.error(request, "wrong username or password")
        return render(request, "login.html", {'form':form})
            

def signout(request):
    logout(request)
    return redirect('signin')

    