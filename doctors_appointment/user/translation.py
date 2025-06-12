# user/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import User

@register(User)
class UserTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')