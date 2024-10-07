from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, Attendance, Payroll
from .forms import EmployeeForm,  AttendanceForm, PayrollForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_list')
    return render(request, 'login.html')

def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employees
    payrolls = Payroll.objects.all()  # Fetch all payrolls
    attendances = Attendance.objects.all()  # Fetch all attendances
    return render(request, 'employee_list.html', {
        'employees': employees, 
        'payrolls': payrolls, 
        'attendances': attendances
    })

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)  # Get employee by primary key (ID)
    return render(request, 'employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee list after creation
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()  # Delete the employee
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})

def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance_form.html', {'form': form})

# View to list attendance records
def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendances': attendances})

def attendance_update(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance_form.html', {'form': form})

def payroll_create(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'payroll_form.html', {'form': form})

# View to list payroll records
def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'payroll_list.html', {'payrolls': payrolls})

# View to update payroll
def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'payroll_form.html', {'form': form})

def payroll_report(request):
    # Create the HTTP response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="payroll_report.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    writer.writerow(['Employee', 'Basic Salary', 'Bonus', 'Deductions', 'Total Pay', 'Date'])

    # Fetch all payroll records
    payrolls = Payroll.objects.all()
    for payroll in payrolls:
        writer.writerow([
            payroll.employee.user.username,
            payroll.salary,
            payroll.bonus,
            payroll.deductions,
            payroll.total_pay,
            payroll.date,
        ])

    return response
