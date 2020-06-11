from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class DeckForm(ModelForm):
    '''
    Form mapping to the deck model
    '''
    class Meta:
        model = Deck
        fields = ['title', 'description', 'is_active']

class CardForm(ModelForm):
    '''
    Form mapping to the card model
    '''
    class Meta:
        model = Card
        fields = ['parentDeck', 'front', 'back']