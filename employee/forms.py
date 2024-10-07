from django import forms
from .models import Employee,Attendance,Payroll

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'position', 'department', 'date_of_joining']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'salary', 'bonus', 'deductions']

    def save(self, commit=True):
        payroll = super().save(commit=False)
        payroll.calculate_total()
        if commit:
            payroll.save()
        return payroll
    
