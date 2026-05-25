from django.db import models

class Sensor(models.Model):
    STATUS_CHOICES = [
        ("normal",  "Normal"),
        ("alerta",  "Alerta"),
        ("critico", "Crítico"),
    ]

    bairro     = models.CharField(max_length=100)
    zona       = models.CharField(max_length=50)
    chuva_mm   = models.FloatField()
    saturacao  = models.FloatField()
    status     = models.CharField(max_length=10, choices=STATUS_CHOICES)
    populacao  = models.CharField(max_length=20)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"
        ordering = ["-chuva_mm"]

    def __str__(self):
        return f"{self.bairro} — {self.chuva_mm}mm ({self.status})"