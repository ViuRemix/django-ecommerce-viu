# app/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    sold_quantity = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_best_seller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    product_images = models.ManyToManyField('ProductImage', related_name='products', blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"

class Slide(models.Model):
    title = models.CharField(max_length=255, verbose_name="Tiêu đề")
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phụ đề")
    image = models.ImageField(upload_to='slides/', verbose_name="Hình ảnh")
    button_text = models.CharField(max_length=50, default="MUA NGAY", verbose_name="Nút CTA")
    button_link = models.URLField(blank=True, null=True, verbose_name="Liên kết nút")

    def __str__(self):
        return self.title

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
# trang cá nhân
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Nam'), ('F', 'Nữ')], default='male')
    image = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Profile"
# yêu thích
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
# sản phẩm xem
class RecentlyViewedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        ordering = ['-viewed_at']

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.full_name}, {self.street_address}, {self.city}, {self.state}, {self.zip_code}, {self.country}'