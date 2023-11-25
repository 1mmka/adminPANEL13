from django.contrib import admin
from app.models import MyTestModel

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name','description','sn_link') # базовые 3
    search_fields = ('name','description')
    list_filter = ('name',)
    
admin.site.register(MyTestModel,MyModelAdmin)