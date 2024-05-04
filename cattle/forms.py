from django import forms
from .models import Cattle, StockType


class CattleForm(forms.ModelForm):

    class Meta:
        model = Cattle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        stock_types = StockType.objects.all()
        names = [(c.id, c.__str__()) for c in stock_types]

        self.fields['name'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'