from django import forms
from .models import StudentList

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = '__all__'  # or list specific fields like ['name', 'age', 'gender', ...]

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
