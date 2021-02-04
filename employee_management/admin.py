from django.contrib import admin

# Register your models here.
from . models  import Employee,EmployeeSalary
admin.site.register(Employee,EmployeeSalary)