document.addEventListener('DOMContentLoaded', function() {
    // Kiểm tra sự tồn tại của carousel
    const carousel = document.querySelector('#carouselExampleAuto');
    if (carousel) {
        const carouselItems = carousel.querySelectorAll('.carousel-item');
        
        carouselItems.forEach(item => {
            item.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
            });
        });
    }

    // Kiểm tra sự tồn tại của các nút category
    const buttons = document.querySelectorAll(".category-btn");
    if (buttons.length > 0) {
        buttons.forEach(button => {
            button.addEventListener("click", function () {
                // Xóa class active khỏi tất cả các nút
                buttons.forEach(btn => btn.classList.remove("active", "btn-dark"));
                
                // Thêm class active vào nút được bấm
                this.classList.add("active", "btn-dark");
            });
        });
    }
    
});

document.addEventListener('DOMContentLoaded', function () {
    const productLinks = document.querySelectorAll('.product-link');

    // Hàm thêm sản phẩm vào danh sách đã xem
    function addToRecentlyViewed(product) {
        let recentlyViewed = JSON.parse(localStorage.getItem('recentlyViewed')) || [];

        // Kiểm tra xem sản phẩm đã tồn tại trong danh sách chưa
        const existingProductIndex = recentlyViewed.findIndex(p => p.id === product.id);
        if (existingProductIndex !== -1) {
            recentlyViewed.splice(existingProductIndex, 1);
        }

        // Thêm sản phẩm vào đầu danh sách
        recentlyViewed.unshift(product);

        // Giới hạn danh sách chỉ lưu tối đa 5 sản phẩm
        if (recentlyViewed.length > 5) {
            recentlyViewed = recentlyViewed.slice(0, 5);
        }

        // Lưu danh sách mới vào localStorage
        localStorage.setItem('recentlyViewed', JSON.stringify(recentlyViewed));
    }

    // Thêm sự kiện click vào từng sản phẩm
    productLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            const product = {
                id: this.getAttribute('data-id'),
                name: this.getAttribute('data-name'),
                price: this.getAttribute('data-price'),
                image: this.getAttribute('data-image')
            };

            // Thêm sản phẩm vào danh sách đã xem
            addToRecentlyViewed(product);
        });
    });
});