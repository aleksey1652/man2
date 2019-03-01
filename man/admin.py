from django.contrib import admin
from .models import mservice,otpr,dapis,bar

class OtprAdmin(admin.ModelAdmin):
    list_display = ('na','')

class MserviceAdmin(admin.ModelAdmin):
    fieldsets = [        
        ('Loh information', {'fields': ['lo']}),
    ]
   
admin.site.register(mservice,MserviceAdmin)
admin.site.register(otpr)
admin.site.register(dapis)
admin.site.register(bar)
# Register your models here.
