from django import forms
from .models import Student, Result

class LoginForm(forms.Form):
    register_number = forms.CharField(label="Register Number")
    dob             = forms.DateField(label="DOB")

class StudentForm(forms.ModelForm):
    class Meta:
        model  = Student
        fields = ["register_number", "dob"]

class ResultForm(forms.ModelForm):
    class Meta:
        model  = Result
        fields = ["student", "semester", "gpa"]
