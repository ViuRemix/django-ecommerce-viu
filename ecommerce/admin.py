from django.contrib import admin
from .models import Category, Product, FeaturedProduct, ProductImage, Slide, CartItem

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

# Đăng ký model Product
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]  # Thêm Inline cho ProductImage
    list_display = ('name', 'category', 'price', 'sale_price', 'is_featured', 'sold_quantity', 'stock','is_new', 'is_sale', 'is_active', 'created_at', 'updated_at', )  # Hiển thị các trường trong danh sách
    list_filter = ('category', 'is_featured', 'is_new', 'is_sale', 'is_active')  # Lọc theo các trường này
    search_fields = ('name', 'description')  # Cho phép tìm kiếm theo tên và mô tả
    prepopulated_fields = {'slug': ('name',)}  # Tự động tạo slug từ tên sản phẩm
    date_hierarchy = 'created_at'  # Cho phép phân loại theo ngày

# Avoid registering the model multiple times
if not admin.site.is_registered(Product):
    admin.site.register(Product, ProductAdmin)

# Đăng ký model FeaturedProduct
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_featured')
    list_filter = ('is_featured',)

admin.site.register(FeaturedProduct, FeaturedProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'image', 'is_active')  # Added 'image' and 'is_active'
    search_fields = ('title', 'subtitle')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'size', 'created_at')
    list_filter = ('user', 'product')
    date_hierarchy = 'created_at'

admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(Slide, SlideAdmin)
admin.site.register(CartItem, CartItemAdmin)