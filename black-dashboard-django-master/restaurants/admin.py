from django.contrib import admin
from .models import Restaurant, MenuItem
from django import forms

class RestaurantChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "Restaurant: {}".format(obj.name)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'opening_hours', 'phone_number', 'rating')
    search_fields = ('name', 'address')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price', 'is_available')
    search_fields = ('name', 'restaurant__name')
    list_filter = ('is_available',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'restaurant':
            return RestaurantChoiceField(queryset=Restaurant.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
