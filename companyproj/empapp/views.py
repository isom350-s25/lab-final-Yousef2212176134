from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm  # Assuming you have a form for Employee

# View to list all employees
def employees(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'employees.html', context)

# View to create a new employee
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')  # Redirect to the employee list view
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', {'form': form})

# View to update an existing employee
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')  # Redirect to the employee list view
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form})

# View to delete an employee
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees')  # Redirect to the employee list view
    return render(request, 'delete_employee.html', {'employee': employee})
