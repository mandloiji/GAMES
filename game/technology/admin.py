from django.contrib import admin
from.models import Tech,NewModel

class TechAdmin(admin.ModelAdmin):
    list_display=('heading','description','image','id')
    
class NewAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','Device','id')
    
admin.site.register(Tech,TechAdmin)
admin.site.register(NewModel,NewAdmin)




# Register your models here.
