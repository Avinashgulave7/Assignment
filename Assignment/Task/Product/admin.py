from django.contrib import admin
from .models import PRODUCT
# Register your models here.
@admin.register(PRODUCT)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','p_name','p_weight','p_price','created_at','updated_at']
