from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    email = forms.EmailField()
    city = forms.CharField(max_length=100)
