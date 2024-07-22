from django.contrib import admin
from .models import Event, News, Merchandise, Officer
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]

@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Merchandise._meta.fields]

@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Officer._meta.fields]
