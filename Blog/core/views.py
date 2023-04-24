from django.shortcuts import render
from core.forms import BandaForm, UserRegisterForm
from core.models import Banda


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def inicio(request):
    return render(request, 'core/index.html')




def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "core/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "core/index.html", {"mensaje":"Datos incorrectos"})

        else:

            return render(request, "core/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "core/login.html", {"form": form})





def register(request):

    if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render(request,"core/login.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
        #form = UserCreationForm()       
        form = UserRegisterForm()     

    return render(request,"core/register.html" ,  {"form":form})





class BandaListView(ListView):
    model = Banda
    template_name = 'core/mostrar_view.html'
    



class BandaDetailView(DetailView):
    model = Banda
    template_name = 'core/detalle_view.html'



class BandaDeleteView(DeleteView):
    model = Banda
    template_name = 'core/delete_confirm_view.html'
    success_url = '/mostrar_view/'



class BandaCreateView(CreateView):
    model = Banda
    template_name = 'core/create_view.html'
    success_url = '/mostrar_view/'
    fields = ['nombre', 'origen', 'descripcion', 'anio_creacion', 'integrantes']



class BandaUpdateView(UpdateView):
    model = Banda
    template_name = 'core/create_view.html'
    success_url = '/mostrar_view/'
    fields = ['nombre','origen', 'descripcion', 'anio_creacion', 'integrantes'] 




