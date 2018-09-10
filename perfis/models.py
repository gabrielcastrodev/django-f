from django.db import models

class Perfil(models.Model):

    usuario = models.CharField(max_length=255, null=False, default='n\na')
    email = models.CharField(max_length=255, null=False, default='n\na')
    telefone = models.CharField(max_length=15, null=False, default='n\na')
    nome_empresa = models.CharField(max_length=255, null=False)
