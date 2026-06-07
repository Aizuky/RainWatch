from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario   # importa o modelo customizado

def login_view(request):
    if request.method == "POST":
        entrada = request.POST.get("usuario")  # pode ser username ou email
        senha = request.POST.get("senha")

        user = None

        user = authenticate(request, username=entrada, password=senha)

        if user is None:
            try:
                usuario_obj = Usuario.objects.get(email=entrada)
                user = authenticate(request, username=usuario_obj.username, password=senha)
            except Usuario.DoesNotExist:
                user = None

        if user:
            login(request, user)
            messages.success(request, "Login realizado com sucesso.")
            return redirect("sensores:dashboard")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, "usuarios/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Você saiu da conta.")
    return redirect("usuarios:login")

def cadastro_view(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirma = request.POST.get("confirma_senha")
        nome = request.POST.get("nome_completo")

        if senha != confirma:
            messages.error(request, "As senhas não coincidem.")
            return redirect("usuarios:cadastro")

        if Usuario.objects.filter(username=usuario).exists():
            messages.error(request, "Já existe um usuário com este nome.")
            return redirect("usuarios:cadastro")

        Usuario.objects.create_user(
            username=usuario,   # usa o campo herdado
            email=email,
            password=senha,
            nome_completo=nome or usuario  # fallback: se nome vier vazio, usa o username
        )

        messages.success(request, "Cadastro realizado com sucesso.")
        return redirect("usuarios:login")

    return render(request, "usuarios/cadastro.html")

def esqueci_senha_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        nova = request.POST.get("nova_senha")
        confirma = request.POST.get("confirma_senha")

        if nova != confirma:
            messages.error(request, "As senhas não coincidem.")
            return render(request, "usuarios/esqueci_senha.html")  # volta pra mesma tela

        usuarios = Usuario.objects.filter(email=email)
        if not usuarios.exists():
            messages.error(request, "Não existe usuário com este email.")
            return render(request, "usuarios/esqueci_senha.html")  # volta pra mesma tela

        if usuarios.count() > 1:
            messages.error(request, "Mais de um usuário usa este email. Informe o usuário também.")
            return render(request, "usuarios/esqueci_senha.html")  # volta pra mesma tela

        user = usuarios.first()
        user.set_password(nova)
        user.save()

        # sucesso → redireciona para login com mensagem positiva
        messages.success(request, "Email enviado com sucesso.")
        return redirect("usuarios:login")

    return render(request, "usuarios/esqueci_senha.html")

@login_required
def perfil_view(request):
    return render(request, "usuarios/perfil.html", {"usuario": request.user})
