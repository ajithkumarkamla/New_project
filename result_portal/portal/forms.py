from django import forms

class LoginForm(forms.Form):
    register_number = forms.CharField(
        label="Register Number",
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "25CS1001"
        })
    )
    dob = forms.DateField(
        label="DOB",
        widget=forms.DateInput(attrs={
            "type": "date", "class": "form-control"
        })
    )
