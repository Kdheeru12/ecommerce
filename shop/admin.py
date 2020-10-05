from django.contrib import admin
from .models import *
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["name","price","image"]
    list_display_links = ["name","image"]
    list_filter = ["price"]
    list_editable =['price']
    list_per_page = 30
    search_fields = ["name","price","avail"]
    class Meta:
        model = Product
admin.site.register(Customer)
admin.site.register(Product,PostModelAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
