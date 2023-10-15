from django.contrib import admin
from myapp2.models import User, Product, Order, Category

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_name', 'category', 'price_product', 'quantity_product']
#     ordering = ['category', '-price_product']
#     list_filter = ['date_add_product', 'price_product']
#     search_fields = ['product_description']
#     search_help_text = 'Поиск по полю Описание продукта (product_description)'


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['product_name', 'category', 'quantity_product']

    """Отдельный продукт."""
    # fields = ['name', 'description', 'category', 'date_added','rating']
    readonly_fields = ['date_add_product']
    fieldsets = [
    (
        None,
        {
            'classes': ['wide'],
            'fields': ['product_name'],
        },
    ),
    (
        'Подробности',
        {
            'classes': ['collapse'],
            'description': 'Категория товара и его подробное описание',
            'fields':['category', 'product_description'],
    },
    ),
    (
        'Бухгалтерия',
        {
            'fields': ['price_product', 'quantity_product'],

        }
    ),
    # (
    #     'Рейтинг и прочее',
    #     {
    #         'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
    #         'fields': ['rating', 'date_added'],
    #     }
    # ),
    ]



admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Category)





