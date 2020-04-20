from django.contrib import admin

from estructura.models import Origen, Marca, Variedad 

# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'lugar', 'sitioweb', 'email')
	search_fields = ('nombre',)
	list_filter = ('nombre',)
	ordering = ('-nombre',)
	raw_id_fields =('lugar',)

class VariedadAdmin(admin.ModelAdmin):
	list_display = ('estilo', 'sabor', 'aroma', 'marca','precio')
	list_filter = ('estilo',)
	ordering = ('-estilo',)
	raw_id_fields =('marca',)



admin.site.register(Origen)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Variedad, VariedadAdmin)
