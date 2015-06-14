from django.contrib import admin
from AGEs.models import Category, Item, Picture

class ItemAdmin(admin.ModelAdmin):
    # 下記を書くことでslugフィールドに自動的にitem_nameが設定される
    prepopulated_fields = {'slug':('item_name',)}
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Picture)
