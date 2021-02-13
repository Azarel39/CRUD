from django.urls import path

from crud.views import *

urlpatterns = [
    path('', index, name='crud-index'),
    path('hola/', hola, name='crud-hola'),
    path('alCuadrado/<int:num>/', al_cuadrado, name='crud-al-cuadrado'),
    path('esPar/<int:num>/', esPar, name='crud-esPar'),
    path('person/', person, name='crud-person'),
    path('dropPerson/<int:pk>/', drop_person, name='crud-drop-person'),
    path('editPerson/<int:pk>/', edit_person, name='crud-edit-person'),
    # http://127.0.0.1:8000/crud/esPar/

]