from django.contrib import admin
from .models import Banner, Workshop, Atividade, Mensagem

# Register your models here.
admin.site.register(Banner)
admin.site.register(Workshop)
admin.site.register(Atividade)
admin.site.register(Mensagem)
