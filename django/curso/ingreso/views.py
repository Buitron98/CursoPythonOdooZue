from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, User

def register_user(request):
    registro_form = UserCreationForm()
    if request.method == 'POST':
        registro_form = UserCreationForm(request.POST)
        if registro_form.is_valid():
            return redirect('login_page')
    return render(request, 'registro.html',{'title':'Registrarse','registro_form':registro_form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index_cliente')
        else:
            mensaje = 'No hemos logrado verificar tu usuario!'
            return render(request, 'login.html', {'title': 'Ingreso','msg_error':mensaje})
    return render(request, 'login.html',{'title':'Ingreso'})

def logout_user(request):
    logout(request)
    return redirect('login_page')



