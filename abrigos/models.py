from django.db import models

class Abrigo(models.Model):
    TIPO_CHOICES = [
        ("Escola",  "Escola"),
        ("Ginásio", "Ginásio"),
        ("Igreja",  "Igreja"),
        ("Centro",  "Centro"),
    ]

    nome        = models.CharField(max_length=200)
    endereco    = models.CharField(max_length=300)
    tipo        = models.CharField(max_length=20, choices=TIPO_CHOICES)
    bairro      = models.CharField(max_length=100)
    capacidade  = models.IntegerField()

    class Meta:
        verbose_name = "Abrigo"
        verbose_name_plural = "Abrigos"
        ordering = ["bairro", "nome"]

    def __str__(self):
        return f"{self.nome} — {self.bairro}"