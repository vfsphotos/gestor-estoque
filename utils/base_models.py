from django.db import models


class BaseModel(models.Model):
    data_criacao = models.DateTimeField(
        auto_now_add=True, 
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True, 
    )

    class Meta:
        abstract = True