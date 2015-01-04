from django import forms

class dataform(forms.Form):
    fname = forms.CharField(label='First name', max_length=100)
    lname = forms.CharField(label='Last name', max_length=30)
    school = forms.CharField(label='School', max_length=100)