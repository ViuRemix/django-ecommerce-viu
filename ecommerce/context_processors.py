def footer_context(request):
    return {
        'about_items': [
            {"name": "Giới thiệu ACFC", "url": "/gioi-thieu"},
            {"name": "Chương trình Khách Hàng Thân Thiết", "url": "/khach-hang-than-thiet"},
            {"name": "Hệ thống cửa hàng", "url": "/cua-hang"},
            {"name": "Tuyển dụng", "url": "/tuyen-dung"},
            {"name": "Liên hệ với chúng tôi", "url": "/lien-he"},
            {"name": "Blog", "url": "/blog"},
        ],
        'support_items': [
            {"name": "Thông tin liên hệ", "url": "/lien-he"},
            {"name": "Hướng dẫn đặt hàng", "url": "/huong-dan-dat-hang"},
            {"name": "Hướng dẫn tạo tài khoản thành viên", "url": "/huong-dan-tao-tai-khoan"},
            {"name": "Hướng dẫn kích hoạt tài khoản thành viên", "url": "/kich-hoat-tai-khoan"},
            {"name": "Chính sách giao hàng", "url": "/chinh-sach-giao-hang"},
            {"name": "Chính sách đổi hàng và bảo hành", "url": "/chinh-sach-doi-hang"},
            {"name": "Chính sách trả góp", "url": "/chinh-sach-tra-gop"},
            {"name": "Hướng dẫn đổi hàng", "url": "/huong-dan-doi-hang"},
            {"name": "Chính sách bảo mật", "url": "/chinh-sach-bao-mat"},
            {"name": "Điều khoản dịch vụ", "url": "/dieu-khoan-dich-vu"},
            {"name": "Quà tặng doanh nghiệp", "url": "/qua-tang-doanh-nghiep"},
        ],
        'social_icons': [
            {'name': 'facebook', 'url': 'https://facebook.com'},
            {'name': 'instagram', 'url': 'https://instagram.com'}, 
            {'name': 'youtube', 'url': 'https://youtube.com'},
            {'name': 'twitter', 'url': 'https://twitter.com'},
            ],
    }
