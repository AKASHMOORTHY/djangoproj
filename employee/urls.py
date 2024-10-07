from django.urls import path
from .views import register, login_view,employee_list, employee_detail, employee_create, employee_update, employee_delete,attendance_create,attendance_list,attendance_update,payroll_list,payroll_create,payroll_update
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('', login_view, name='login'),
    path('employee_list', employee_list, name='employee_list'),
    path('<int:pk>/', employee_detail, name='employee_detail'),
    path('create/', employee_create, name='employee_create'),
    path('<int:pk>/update/', employee_update, name='employee_update'),
    path('<int:pk>/delete/', employee_delete, name='employee_delete'),
    path('attendance/', attendance_list, name='attendance_list'),
    path('attendance/new/', attendance_create, name='attendance_create'),
    path('attendance/<int:pk>/edit/',attendance_update, name='attendance_update'),
    path('payroll/',payroll_list, name='payroll_list'),
    path('payroll/new/',payroll_create, name='payroll_create'),
    path('payroll/<int:pk>/edit/',payroll_update, name='payroll_update'),

    path('payroll/', views.payroll_list, name='payroll_list'),
    path('payroll/new/', views.payroll_create, name='payroll_create'),
    path('payroll/<int:pk>/edit/', views.payroll_update, name='payroll_update'),
    path('payroll/report/', views.payroll_report, name='payroll_report'),

]
