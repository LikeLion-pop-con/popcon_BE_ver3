from django.contrib import admin
from .models import *

admin.site.register(Brand)
admin.site.register(Popup)
admin.site.register(Category)
admin.site.register(BrandCategory)
admin.site.register(PopupReservation)


#admin.site.register(BrandImage)