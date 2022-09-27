from .models import HomeCustomer, HomeCustomerActive, HomeInfo, HomeProduct, HomeSlider, HomeSliderActive, About, Product
from modeltranslation.translator import register, TranslationOptions


@register(HomeCustomer)
class HomeCustomerTranslationOptions(TranslationOptions):
    fields = ('name', 'about')

@register(HomeCustomerActive)
class HomeCustomerActiveTranslationOptions(TranslationOptions):
    fields = ('name', 'about')