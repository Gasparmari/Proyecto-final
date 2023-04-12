
from django.contrib import admin
from django.urls import path
from core.views import inicio, BandaListView, BandaDeleteView, BandaDetailView, BandaCreateView, BandaUpdateView

urlpatterns = [
    path('', inicio , name='index'),
    path('mostrar_view/', BandaListView.as_view() , name='mostrar_view'),
    path('borrar/<int:pk>/', BandaDeleteView.as_view(), name= 'delete_view'),
    path('nuevo/', BandaCreateView.as_view(), name= 'new_view'),
    path('<int:pk>/', BandaDetailView.as_view(), name= 'detail_view'),
    path('editar_view/<int:pk>/', BandaUpdateView.as_view(), name= 'update_view')


]
