from django.db import models

# Create your models here.

class Lead(models.Model):
    """
    Representa um lead capturado pelo formulário.
    """
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome