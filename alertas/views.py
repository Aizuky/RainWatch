from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .servico import _disparar
from .models import Alerta, ConfiguracaoAlerta
from .servico import processar_sensores
from sensores.dados import SENSORES


# Tela de alertas

@login_required
def painel(request):
    alertas = Alerta.objects.all()[:100]
    configs = ConfiguracaoAlerta.objects.all()

    total     = alertas.count() if hasattr(alertas, "count") else len(alertas)
    enviados  = sum(1 for a in alertas if a.status == "enviado")
    falhas    = sum(1 for a in alertas if a.status == "falha")
    pendentes = sum(1 for a in alertas if a.status == "pendente")

    ctx = {
        "alertas": alertas,
        "configs": configs,
        "total": total,
        "enviados": enviados,
        "falhas": falhas,
        "pendentes": pendentes,
    }
    return render(request, "alertas/painel.html", ctx)

# Disparar alertas manualmente

@require_POST
def disparar(request):
    criados = processar_sensores(SENSORES)
    n = len(criados)
    if n:
        messages.success(request, f"{n} alerta(s) gerado(s) e processado(s) com sucesso.")
    else:
        messages.info(request, "Nenhum sensor em nível de alerta ou crítico no momento.")
    return redirect("alertas:painel")

# Criar configuração de alerta

def config_criar(request):
    if request.method == "POST":
        nome             = request.POST.get("nome", "").strip()
        canal            = request.POST.get("canal", "email")
        destinatario     = request.POST.get("destinatario", "").strip()
        notif_alerta     = request.POST.get("notificar_alerta") == "on"
        notif_critico    = request.POST.get("notificar_critico") == "on"

        if not nome or not destinatario:
            messages.error(request, "Nome e destinatário são obrigatórios.")
        else:
            ConfiguracaoAlerta.objects.create(
                nome=nome,
                canal=canal,
                destinatario=destinatario,
                notificar_alerta=notif_alerta,
                notificar_critico=notif_critico,
            )
            messages.success(request, f"Configuração '{nome}' criada com sucesso.")
            return redirect("alertas:painel")

    return render(request, "alertas/config_form.html", {"acao": "Criar"})

# Editar configuração

def config_editar(request, pk):
    cfg = get_object_or_404(ConfiguracaoAlerta, pk=pk)

    if request.method == "POST":
        cfg.nome              = request.POST.get("nome", cfg.nome).strip()
        cfg.canal             = request.POST.get("canal", cfg.canal)
        cfg.destinatario      = request.POST.get("destinatario", cfg.destinatario).strip()
        cfg.notificar_alerta  = request.POST.get("notificar_alerta") == "on"
        cfg.notificar_critico = request.POST.get("notificar_critico") == "on"
        cfg.ativo             = request.POST.get("ativo") == "on"
        cfg.save()
        messages.success(request, f"Configuração '{cfg.nome}' atualizada.")
        return redirect("alertas:painel")

    return render(request, "alertas/config_form.html", {"acao": "Editar", "cfg": cfg})

# Excluir configuração

@require_POST
def config_excluir(request, pk):
    cfg = get_object_or_404(ConfiguracaoAlerta, pk=pk)
    nome = cfg.nome
    cfg.delete()
    messages.success(request, f"Configuração '{nome}' removida.")
    return redirect("alertas:painel")

# Marcar alerta como ignorado

@require_POST
def ignorar_alerta(request, pk):
    alerta = get_object_or_404(Alerta, pk=pk)
    alerta.status = "ignorado"
    alerta.save()
    return JsonResponse({"ok": True})

# Reenviar alerta com falha

@require_POST
def reenviar_alerta(request, pk):

    alerta = get_object_or_404(Alerta, pk=pk)
    sensor = {
        "bairro": alerta.bairro,
        "zona": alerta.zona,
        "status": alerta.nivel,
        "chuva_mm": alerta.chuva_mm,
        "saturacao": alerta.saturacao,
    }
    _disparar(alerta, sensor)
    return JsonResponse({"ok": True, "status": alerta.status})
