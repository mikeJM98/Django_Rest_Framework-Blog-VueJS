from django.contrib import admin

# Register your models here.
from .models import DemandaAlimentos, HijosDelDemandado

# Register your models here.
admin.site.register(DemandaAlimentos)
admin.site.register(HijosDelDemandado)