from django import forms
from .models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
        labels = {
            'nombre': 'Nombre del Autor:',
            'apellidos': 'Apellidos del Autor:',
            'nacionalidad': 'Nacionalidad del Autor:',
            'descripcion': 'Pequeña Descripción:',
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Nombre del Autor',
                    'id': 'nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Apellido del Autor',
                    'id': 'apellidos'
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nacionalidad del Autor',
                    'id': 'nacionalidad'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Descripción del Autor',
                    'id': 'descripcion'
                }
            )
        }