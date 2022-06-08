from django.contrib import admin
from .models import Dog, Cat, Car, Horse

admin.site.register(Car)
admin.site.register(Cat)
admin.site.register(Dog)
admin.site.register(Horse)
