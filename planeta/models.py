from uuid import uuid4
from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator, MaxValueValidator
from planeta import ABRIGA_VIDA_CHOICE


class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    create_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    update_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        abstract = True


class Planeta(BaseModel):

    nome = models.CharField(_('Nome'), max_length=200)
    porcetagem_agua = models.FloatField(_('Porcentagem de água'),
                                        validators=[MinValueValidator(0), MaxValueValidator(100)])
    distancia = models.IntegerField(_('Distância'), validators=[MinValueValidator(0)])
    abriga_vida = models.CharField(_('Abriga vida'), max_length=3, choices=ABRIGA_VIDA_CHOICE.items())

    @property
    def elemetos_resumido(self):
        elementos = list(self.elementos.all())
        qtd = len(elementos)
        if qtd == 0:
            return 'Nenhum elemento cadastrado.'

        resumo = ', '.join((str(elemento) for i, elemento in enumerate(elementos) if i < 4))
        if qtd > 3:
            return resumo + '...'
        return resumo

    def __str__(self) -> str:
        if len(self.nome) > 15:
            return self.nome[:15] + '...'
        return self.nome


class Elemento(BaseModel):

    planeta = models.ForeignKey(Planeta, verbose_name=_("Planeta"), on_delete=models.CASCADE, related_name='elementos')
    nome = models.CharField(_('Nome'), max_length=200)

    def __str__(self) -> str:
        if len(self.nome) > 15:
            return self.nome[:15] + '...'
        return self.nome
