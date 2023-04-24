
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from core import views
from django.urls import path
from core.views import inicio, BandaListView, BandaDeleteView, BandaDetailView, BandaCreateView, BandaUpdateView, login_request, register

urlpatterns = [
    path('', inicio , name='index'),
    path('mostrar_view/', BandaListView.as_view() , name='mostrar_view'),
    path('borrar/<int:pk>/', BandaDeleteView.as_view(), name= 'delete_view'),
    path('nuevo/', BandaCreateView.as_view(), name= 'new_view'),
    path('<int:pk>/', BandaDetailView.as_view(), name= 'detail_view'),
    path('editar_view/<int:pk>/', BandaUpdateView.as_view(), name= 'update_view'),
    path('login', views.login_request, name="login"),
    path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(template_name='core/logout.html'), name="logout"),

]
