from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentList
from .forms import StudentForm

# List View
def stdlist(request):
    stds = StudentList.objects.all()
    return render(request, "list.html", {"stds": stds})

# Add Student View
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stdlist')
    else:
        form = StudentForm()
    return render(request, 'addform.html', {'form': form})

# Update Student View
def update_student(request, pk):
    student = get_object_or_404(StudentList, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('stdlist')
    else:
        form = StudentForm(instance=student)
    return render(request, 'addform.html', {'form': form})

# Delete Student View
def delete_student(request, pk):
    student = get_object_or_404(StudentList, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('stdlist')
    return render(request, 'confirm_delete.html', {'student': student})
