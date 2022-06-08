from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Authored)
admin.site.register(Book)
##
admin.site.register(Author_2)
admin.site.register(Book_2)