from django.db import models

# Create your models here.

class Lead(models.Model):
    """
    Representa um lead capturado pelo formulário.
    """

    STATUS_CHOICES = [
        ('NOVO', 'Novo'),
        ('EM_CONTATO', 'Em Contato'),
        ('CONVERTIDO', 'Convertido'),
        ('PERDIDO', 'Perdido'),
    ]
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOVO')
    empresa = models.CharField(max_length=255, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome