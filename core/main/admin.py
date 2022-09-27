from django.contrib import admin
from .models import HomeSliderActive, HomeSlider, HomeInfo, HomeProduct, HomeCustomer, HomeCustomerActive, About
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class HomeCustomerAdmin(TranslationAdmin):
    pass 
admin.site.register(HomeCustomer)

class HomeCustomerActiveAdmin(TranslationAdmin):
    pass
admin.site.register(HomeCustomerActive)

admin.site.register(HomeSlider)
admin.site.register(HomeSliderActive)
admin.site.register(HomeInfo)
admin.site.register(HomeProduct)
admin.site.register(About)





