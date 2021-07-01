from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #exigir autenticação nessa página
    path('conta/', views.conta, name='conta'),
]