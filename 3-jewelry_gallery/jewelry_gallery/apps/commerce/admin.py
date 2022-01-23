from django.contrib import admin
from .models import ProductCategory,ProductProperty,Product,Attribute
# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('CategoryTitle','CategoryStatus')
    search_fields = ('CategoryStatus',)
    prepopulated_fields = {'Slug':('CategoryTitle',)}

@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    list_display = ('PropertyTitle','ProductPropertyStatus')
    search_fields = ('ProductPropertyStatus',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Title','Brand','Price','Discount','Status')
    search_fields = ('Status','Discount','Star')
    prepopulated_fields = {'Slug':('Title','Brand')}

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('ProductProperty','Value','AttributeStatus')
    search_fields = ('AttributeStatus',)
