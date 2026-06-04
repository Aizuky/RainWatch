from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        user = authenticate(request, username=usuario, password=senha)
        if user:
            login(request, user)
            messages.success(request, "Login realizado com sucesso.")
            return redirect("dashboard")  # ajuste para sua tela principal
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, "usuarios/login.html")


def cadastro_view(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Verifica se já existe usuário com esse email
        if User.objects.filter(username=email).exists():
            messages.error(request, "Já existe um usuário com este email.")
            return redirect("usuarios:cadastro")

        # Cria o usuário
        User.objects.create_user(
            username=email,   # usamos o email como username
            email=email,
            password=senha,
            first_name=nome
        )

        messages.success(request, "Cadastro realizado com sucesso.")
        return redirect("usuarios:login")

    return render(request, "usuarios/cadastro.html")


def reset_senha_view(request):
    if request.method == "POST":
        nova = request.POST.get("nova_senha")
        confirma = request.POST.get("confirma_senha")

        if nova == confirma:
            request.user.set_password(nova)
            request.user.save()
            messages.success(request, "Senha alterada com sucesso.")
            return redirect("usuarios:login")
        else:
            messages.error(request, "As senhas não coincidem.")
            return redirect("usuarios:esqueci_senha")

    return render(request, "usuarios/esqueci_senha.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Você saiu da conta.")
    return redirect("usuarios:login")

@login_required
def perfil_view(request):
    return render(request, "usuarios/perfil.html", {"usuario": request.user})

@login_required
def perfil_view(request):
    return render(request, "usuarios/perfil.html", {"usuario": request.user})

def logout_view(request):
    logout(request)  # encerra a sessão
    return redirect("usuarios:login")  # redireciona para a tela de login