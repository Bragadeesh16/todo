from django.forms import ModelForm
from .models import todo

class todo_from(ModelForm):
    class Meta:
        model = todo
        fields = '__all__'