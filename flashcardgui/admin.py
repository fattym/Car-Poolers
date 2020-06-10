from django.contrib import admin

# Register your models here.
from api.models import Deck


class DeckAdmin(admin.ModelAdmin):
        pass

admin.site.register(Deck, DeckAdmin)