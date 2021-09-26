from django import forms


class UserForm(forms.Form):
    date_of_birth_from = forms.DateField()
    to = forms.DateField()
