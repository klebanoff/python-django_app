from django import forms


class TwoDatesForm(forms.Form):
    """Form with two date fields: date of birth from and date of birth to"""

    date_of_birth_from = forms.DateField()
    to = forms.DateField()
class OneDateForm(forms.Form):
    """Form with one date of birth date field"""
    date_of_birth = forms.DateField()
