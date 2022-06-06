from django import forms


# creating a form
class TodoForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
