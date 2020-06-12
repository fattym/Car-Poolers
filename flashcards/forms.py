from django.forms import ModelForm
from django import forms
from .models import Deck, Card, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=80, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
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
