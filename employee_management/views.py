from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.
def Employee_add(request):
    form = EmployeeForm()
    print(form)
    return  render (request,"employee_management/employee_insert.html",{'form':form})

def Employee_view(request):
   
    return  render (request,"employee_management/employee_view.html")
    


def Employee_delete(request):
    return