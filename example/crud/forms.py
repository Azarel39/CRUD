from django import forms

from crud.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Nombre de la persona"}),
            'last_name': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Apellido"}),
            'phone': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Telefono"}),
            'email': forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Email"}),
        }
