from django import forms



class BandaForm(forms.Form):
    name = forms.CharField(max_length=20)
    origen = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=1000)
    anio_creacion = forms.CharField(max_length=20)
    integrantes = forms.CharField(max_length=20)
    