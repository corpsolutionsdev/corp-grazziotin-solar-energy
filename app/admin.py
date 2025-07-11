from django.contrib import admin
from .models import QuemSomos, Contato

# Configurar o admin site
admin.site.site_header = "Grazziotin Energia Solar"

admin.site.register(QuemSomos)
admin.site.register(Contato)
