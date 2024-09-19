from typing import Any
from django.db import models

# Create your models here.
class Mensaje(models.Model):
    texto = models.TextField()
    emisor = models.CharField(max_length=100)
    receptor = models.CharField(max_length=100)
    fechaEnvio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de: {self.emisor} \nPara: {self.receptor}\n\n {self.texto}"