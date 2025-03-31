# ecommerce/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import Product, Slide, CartItem, Category,Profile
from django.contrib import messages
from django.views.decorators.http import require_POST
# login
from .models import RecentlyViewedProduct,Favorite
from .forms import ProfileUpdateForm
# thêm sửa xóa địa chỉ
from .models import Address
from .forms import AddressForm

from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.db.models import Q
import logging

logger = logging.getLogger(__name__)  # Add this line to define the logger

def home(request):
    slides = Slide.objects.filter(is_active=True)  # Ensure only active slides are retrieved
    categories = Category.objects.filter(is_active=True)  # Add categories if needed
    featured_products = Product.objects.filter(is_featured=True, is_active=True)  # Add featured products if needed
    new_arrivals = Product.objects.filter(is_new=True, is_active=True)  # Add new arrivals if needed
    brands = ["Brand A", "Brand B", "Brand C"]  # Example brands, replace with actual data if available

    context = {
        'slides': slides,
        'categories': categories,
        'featured_products': featured_products,
        'new_arrivals': new_arrivals,
        'brands': brands,
    }
    return render(request, 'app/home.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart_items_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    if request.method == 'POST':
        size = request.POST.get('size')
        return add_to_cart(request, product_id, size)
    return render(request, 'app/product_detail.html', {'product': product, 'cart_items_count': cart_items_count})

@login_required
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    if product.stock <= 0:
        return JsonResponse({'success': False, 'message': 'Sản phẩm đã hết hàng!'})

    size = request.POST.get('size', 'M')
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        size=size,
        defaults={'quantity': 1}
    )
    if not created:
        if cart_item.quantity + 1 > product.stock:
            return JsonResponse({'success': False, 'message': 'Số lượng vượt quá hàng tồn kho!'})
        cart_item.quantity += 1
    cart_item.save()
    
    cart_items_count = CartItem.objects.filter(user=request.user).count()
    return JsonResponse({
        'success': True,
        'message': f'Đã thêm {product.name} vào giỏ hàng!',
        'cart_items_count': cart_items_count
    })

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_items_with_total = []
    for item in cart_items:
        item_total = item.quantity * float(item.product.price)
        cart_items_with_total.append({
            'item': item,
            'total': item_total
        })
    total_price = sum(item.quantity * float(item.product.price) for item in cart_items)
    cart_items_count = cart_items.count()
    return render(request, 'app/addcart.html', {
        'cart_items': cart_items_with_total,
        'total_price': total_price,
        'cart_items_count': cart_items_count
    })

@login_required
@require_POST
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        new_size = request.POST.get('size', cart_item.size)  # Lấy kích thước mới

        if 0 < quantity <= cart_item.product.stock:
            cart_item.quantity = quantity
            cart_item.size = new_size  # Cập nhật kích thước
            cart_item.save()
            messages.success(request, "Đã cập nhật giỏ hàng!")
        else:
            messages.error(request, "Số lượng không hợp lệ hoặc vượt quá hàng tồn kho!")

    cart_items = CartItem.objects.filter(user=request.user)
    cart_items_with_total = []
    for item in cart_items:
        item_total = item.quantity * float(item.product.price)
        cart_items_with_total.append({
            'item': item,
            'total': item_total
        })
    total_price = sum(item.quantity * float(item.product.price) for item in cart_items)
    return render(request, 'app/addcart.html', {
        'cart_items': cart_items_with_total,
        'total_price': total_price
    })

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Đã xóa sản phẩm khỏi giỏ hàng!")
    return redirect('view_cart')


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    if not cart_items.exists():
        messages.error(request, "Giỏ hàng trống. Thêm sản phẩm trước khi thanh toán.")
        return redirect('view_cart')

    cart_items_with_total = []
    for item in cart_items:
        item_total = item.quantity * float(item.product.price)
        cart_items_with_total.append({
            'item': item,
            'total': item_total,
            'image': item.product.image.url if item.product.image else None
        })
    total_price = sum(item.quantity * float(item.product.price) for item in cart_items)

    return render(request, 'app/checkout.html', {
        'cart_items': cart_items_with_total,
        'total_price': total_price
    })


@login_required
def process_checkout(request):
    if request.method == "POST":
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return HttpResponse("Giỏ hàng trống!", status=400, content_type="text/html; charset=utf-8")
        
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        if not all([name, phone, address]):
            return HttpResponse("Điền đầy đủ thông tin!", status=400, content_type="text/html; charset=utf-8")
        
        total_price = sum(item.quantity * float(item.product.price) for item in cart_items)
        cart_items.delete()  # Xóa giỏ hàng sau thanh toán
        
        return HttpResponse("Thanh toán thành công!", content_type="text/html; charset=utf-8")
    return redirect("checkout")

def san_pham(request):
    products = Product.objects.filter(is_active=True)
    cart_items_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'app/san_pham.html', {'products': products, 'cart_items_count': cart_items_count})

def giay_dep(request):
    products = Product.objects.filter(category__name="Giày dép", is_active=True)
    cart_items_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'app/giay_dep.html', {'products': products, 'cart_items_count': cart_items_count})

def tui_vi(request):
    products = Product.objects.filter(category__name="Túi ví", is_active=True)
    cart_items_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'app/tui_vi.html', {'products': products, 'cart_items_count': cart_items_count})

def phu_kien(request):
    products = Product.objects.filter(category__name="Phụ kiện", is_active=True)
    cart_items_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'app/phu_kien.html', {'products': products, 'cart_items_count': cart_items_count})

def giam_gia(request):
    products = Product.objects.filter(is_active=True).order_by('-price')[:10]
    cart_items_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'app/giam_gia.html', {'products': products, 'cart_items_count': cart_items_count})

def about(request):
    cart_items_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'app/about.html', {'cart_items_count': cart_items_count})

# đăng ký
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Đăng ký thành công!")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})

# tìm kiếm
def search_products(request):
    query = request.GET.get('q', '')  # Lấy giá trị tìm kiếm từ thanh search
    products = Product.objects.filter(name__icontains=query) if query else []
    
    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'app/search_results.html', context)

# Trang cá nhân
@login_required
def profile_view(request):
    user = request.user
    # Ensure Profile exists
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Cập nhật thông tin thành công!")
            return redirect('profile')
        else:
            # Log form errors for debugging
            print(profile_form.errors)
            messages.error(request, "Có lỗi xảy ra, vui lòng kiểm tra lại.")
    else:
        profile_form = ProfileUpdateForm(instance=profile)

    favorites = Favorite.objects.filter(user=user)
    recently_viewed = RecentlyViewedProduct.objects.filter(user=user).select_related('product').order_by('-viewed_at')[:10]
    addresses = Address.objects.filter(user=user)  # Get addresses for the logged-in user
    address_form = AddressForm()  # Initialize an empty address form

    context = {
        'profile_form': profile_form,
        'favorites': favorites,
        'recently_viewed': recently_viewed,
        'addresses': addresses,  # Add addresses to the context
        'address_form': address_form,  # Add address form to the context
    }
    return render(request, 'app/profile.html', context)


# yêu thích
@login_required
def add_to_favorites(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=user, product=product)
    if created:
        message = "Sản phẩm đã được thêm vào danh sách yêu thích!"
    else:
        message = "Sản phẩm đã có trong danh sách yêu thích!"
    return JsonResponse({'success': True, 'message': message})
@login_required
def favorites_view(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    context = {
        'favorites': favorites,
    }
    return render(request, 'app/favorites.html', context)
# thêm sửa xóa địa chỉ

@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('profile')
    return redirect('profile')

@login_required
def edit_address(request, address_id):
    address = get_object_or_404(Address, id=address_id, user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return redirect('profile')

@login_required
def delete_address(request, address_id):
    address = get_object_or_404(Address, id=address_id, user=request.user)
    if request.method == 'POST':
        address.delete()
        return redirect('profile')
    return redirect('profile')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

# category_detail
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, is_active=True)  # Lọc sản phẩm theo danh mục

    return render(request, 'app/category_detail.html', {'category': category, 'products': products})