from django.forms import ModelForm, TextInput, HiddenInput
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }),
            'user': HiddenInput(),           
        }

class UserCreate(UserCreationForm):
    class Meta:
        model= User
        fields = ['username','email', 'password1', 'password2']

        widgets = {

        }