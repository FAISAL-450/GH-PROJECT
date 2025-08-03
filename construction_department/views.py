from django.shortcuts import render
def construction_department_view(request):
    return render(request, 'construction_department/construction_department.html')  # Corrected path
