from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def list_users(request):
    users = User.objects.all()
    return render(request, 'list_users.html', {'users': users})


def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        description = request.POST['description']
        user = User.objects.create(
            name=name, surname=surname, email=email, password=password, description=description)
        user.save()
    return redirect('/users/')


def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users/')


def edit_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        description = request.POST['description']

        # Actualizar los campos del usuario existente
        user.name = name
        user.surname = surname
        user.email = email
        user.password = password
        user.description = description
        user.save()

        return redirect('/users/')

    return render(request, 'edit_user.html', {'user': user})
