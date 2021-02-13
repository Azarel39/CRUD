from builtins import range

from django.shortcuts import render, redirect

# Create your views here.
from crud.forms import PersonForm
from crud.models import Person


def index(request):
    arreglo = []
    for i in range(5):
        arreglo.append({
            'id': i,
            'nombre': f'Posición {i + 1}',
        })
    data = {
        'message': 'Hola desde la vista',
        'arreglo': arreglo
    }
    return render(request, 'crud/index.html', data)


def hola(request):
    data = {
        'message': 'Hola desde http://127.0.0.1:8000/crud/hola'
    }
    return render(request, 'crud/index.html', data)


def al_cuadrado(request, num):
    data = {
        'message': f'El cuadrado de {num} es {num * num}'
    }
    return render(request, 'crud/index.html', data)


def esPar(request, num):
    message = ''
    if num % 2 == 0:
        message = f'El numero {num} es par'
    else:
        message = f'El numero {num} es par'

    data = {'message': message}

    return render(request, 'crud/index.html', data)


def person(request):
    person_form = PersonForm()
    errors = False
    created = False
    if request.method == 'POST':
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            person_form.save()
            created = 'Persona creada'
            person_form = PersonForm()
        else:
            errors = person_form.errors

    persons = Person.objects.filter(is_active=True)
    data = {
        'person_form': person_form,
        'errors': errors,
        'created': created,
        'persons': persons,
    }
    return render(request, 'crud/person.html', data)


def drop_person(request, pk):
    person = Person.objects.get(id=pk)
    person.is_active = False
    person.save()
    person_form = PersonForm()
    errors = False
    created = 'Persona borrada'
    persons = Person.objects.filter(is_active=True)
    data = {
        'person_form': person_form,
        'errors': errors,
        'created': created,
        'persons': persons,
    }
    return render(request, 'crud/person.html', data)


def edit_person(request, pk):
    person = Person.objects.get(id=pk)
    if request.method == "POST":
        person_form = PersonForm(request.POST, instance=person)
        if person_form.is_valid():
            person_form.save()
            return redirect('/crud/person/')
    else:
        person_form = PersonForm(instance=person)
    data = {
        'person_form': person_form,
        'pk': pk,
    }
    return render(request, 'crud/edit-person.html', data)
