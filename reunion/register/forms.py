from django import forms


class RegistroForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su nombre'}
    ), min_length=3, max_length=200)
    apPat = forms.CharField(label="Apellido Paterno", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su apellido paterno'}
    ), min_length=3, max_length=200)
    apMat = forms.CharField(label="Apellido Materno", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su apellido materno'}
    ), min_length=3, max_length=200)
    email = forms.EmailField(label="Correo Electrónico", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su correo electrónico'}
    ), min_length=3, max_length=200)
    telefono = forms.CharField(label="Teléfono", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder':'Ingrese su teléfono incluyendo lada'}
    ), min_length=3, max_length=25)
    grado = forms.CharField(label="Grado Académico", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su grado académico'}
    ), min_length=3, max_length=200)
    siglas = forms.CharField(label="Siglas de Grado", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese las siglas de su grado académico'}
    ))
    puesto = forms.CharField(label="Puesto", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su puesto'}
    ), min_length=3, max_length=200)
    
    