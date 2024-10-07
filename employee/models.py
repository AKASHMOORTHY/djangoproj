from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # Present, Absent, etc.

    def __str__(self):
        return f"{self.employee.user.username} - {self.date} - {self.status}"

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateField(auto_now_add=True)

    def calculate_total(self):
        self.total_pay = self.salary + self.bonus - self.deductions
        return self.total_pay

    def __str__(self):
        return f"{self.employee.user.username} - {self.date} - {self.total_pay}"