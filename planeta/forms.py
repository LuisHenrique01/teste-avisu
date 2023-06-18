from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from planeta.models import Planeta, Elemento


class PlanetaForm(ModelForm):

    class Meta:
        model = Planeta
        fields = '__all__'


class ElementoForm(ModelForm):

    class Meta:
        model = Elemento
        fields = '__all__'


ElementoFormSet = inlineformset_factory(Planeta, Elemento, form=ElementoForm, extra=1, can_delete=False)
UpdateElementoFormSet = inlineformset_factory(Planeta, Elemento, form=ElementoForm, extra=0, can_delete=True, edit_only=True)