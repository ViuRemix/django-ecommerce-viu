from django.contrib import admin
from .models import Category, Product, ProductImage, Slide, CartItem

# Inline để hiển thị các ảnh sản phẩm liên quan đến Product trong Django Admin
class ProductImageInline(admin.TabularInline):
    model = Product.product_images.through  # Liên kết với mối quan hệ ManyToMany
    extra = 1  # Số lượng ô nhập thêm ảnh mặc định

# Admin cho Product
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]  # Hiển thị hình ảnh của sản phẩm trong tab sản phẩm
    list_display = ('name', 'price', 'stock', 'is_active', 'created_at')  # Các cột hiển thị
    list_filter = ('category', 'is_active', 'is_best_seller')  # Lọc
    search_fields = ('name', 'description')  # Tìm kiếm
    date_hierarchy = 'created_at'  # Phân cấp theo thời gian

# Admin cho Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Hiển thị tên danh mục
    search_fields = ('name',)  # Tìm kiếm theo tên

# Admin cho Slide
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'button_text', 'button_link')  # Các cột hiển thị
    search_fields = ('title', 'subtitle')  # Tìm kiếm

# Admin cho CartItem
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'size', 'created_at')  # Các cột hiển thị
    list_filter = ('user', 'product')  # Lọc
    date_hierarchy = 'created_at'  # Phân cấp theo thời gian

# Đăng ký các mô hình với admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Slide, SlideAdmin)
admin.site.register(CartItem, CartItemAdmin)