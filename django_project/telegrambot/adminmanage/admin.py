from django.contrib import admin
from .models import User, Category, SubCategory, Product, Order, OrderItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'username', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'username', 'email')
    list_filter = ('created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'title', 'price', 'available', 'created_at', 'updated_at')
    list_filter = ('subcategory', 'available')
    search_fields = ('title',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'is_processed', 'quantity', 'order_time',
                    'email', 'receiver', 'successful')
    list_filter = ('is_processed', 'successful', 'order_time')
    search_fields = ('user__name', 'user__username', 'receiver', 'email')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_filter = ('order', 'product')
    search_fields = ('order__id', 'product__title')

    inlines = [
        OrderItemInline,
    ]
