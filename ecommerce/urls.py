from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import favorites_view, add_to_favorites

urlpatterns = [
    path('', views.home, name='home'),
    path('san-pham/', views.san_pham, name='san_pham'),
    path('giay-dep/', views.giay_dep, name='giay_dep'),
    path('tui-vi/', views.tui_vi, name='tui_vi'),
    path('phu-kien/', views.phu_kien, name='phu_kien'),
    path('giam-gia/', views.giam_gia, name='giam_gia'),
    path('about/', views.about, name='about'),
    path('san-pham/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),  # Thêm dòng này
    path('checkout/', views.checkout, name='checkout'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/register/', views.register, name='register'),
    # yêu thích
    path('favorites/', favorites_view, name='favorites'),
    path('add_to_favorites/<int:product_id>/', add_to_favorites, name='add_to_favorites'),
    path('profile/', views.profile_view, name='profile'),  # trang profile khi đã đăng nhập
    path('search/', views.search_products, name='search_products'),
    # thêm sửa xóa địa chỉ
    path('add_address/', views.add_address, name='add_address'),
    path('edit_address/<int:address_id>/', views.edit_address, name='edit_address'),
    path('delete_address/<int:address_id>/', views.delete_address, name='delete_address'),
]