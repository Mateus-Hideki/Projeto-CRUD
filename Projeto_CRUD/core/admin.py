from django.contrib import admin
from .admin_site import admin_site
from .models import Categoria, Modelo, Roupa

admin_site.register(Categoria)
admin_site.register(Modelo)
admin_site.register(Roupa)
