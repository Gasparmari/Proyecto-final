from django.shortcuts import render
from core.forms import BandaForm
from core.models import Banda


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def inicio(request):
    return render(request, 'core/index.html')



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
    fields = ['nombre','origen', 'descripcion', 'anio_creacion', 'integrantes']



class BandaUpdateView(UpdateView):
    model = Banda
    template_name = 'core/create_view.html'
    success_url = '/mostrar_view/'
    fields = ['nombre','origen', 'descripcion', 'anio_creacion', 'integrantes'] 




