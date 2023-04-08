from django.forms import ModelForm, Textarea, TextInput
from .models import Todo

class TodoForm(ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }),
            
        }