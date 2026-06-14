from django.shortcuts import render
from .models import Abrigo
from sensores.models import Sensor

def lista_abrigos(request):
    bairro_filtro = request.GET.get("bairro", "")
    busca = request.GET.get("busca", "")

    bairros = Abrigo.objects.values_list("bairro", flat=True).distinct().order_by("bairro")
    status_por_bairro = {s.bairro: s.status for s in Sensor.objects.all()}

    abrigos = Abrigo.objects.all()

    if bairro_filtro:
        abrigos = abrigos.filter(bairro=bairro_filtro)

    if busca:
        abrigos = abrigos.filter(nome__icontains=busca)

    abrigos_com_risco = []
    for a in abrigos:
        abrigos_com_risco.append({
            "id": a.id,
            "nome": a.nome,
            "endereco": a.endereco,
            "tipo": a.tipo,
            "bairro": a.bairro,
            "capacidade": a.capacidade,
            "risco": status_por_bairro.get(a.bairro, "normal"),
        })

    contexto = {
        "abrigos": abrigos_com_risco,
        "bairros": bairros,
        "bairro_selecionado": bairro_filtro,
        "busca": busca,
        "total": len(abrigos_com_risco),
    }
    return render(request, "abrigos/abrigos.html", contexto)