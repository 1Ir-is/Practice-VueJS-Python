<template>
  <section class="featured-books">
    <div class="container">
      <div class="section-header">
        <h2>Sách Nổi Bật</h2>
        <p>Những cuốn sách được yêu thích nhất tại cửa hàng của chúng tôi</p>
      </div>

      <div class="books-grid">
        <div class="book-card" v-for="book in featuredBooks" :key="book.id">
          <div class="book-image">
            <img :src="book.image" :alt="book.title" />
            <div class="book-overlay">
              <button class="btn-quick-view">Xem Nhanh</button>
            </div>
          </div>
          <div class="book-info">
            <h3 class="book-title">{{ book.title }}</h3>
            <p class="book-author">{{ book.author }}</p>
            <div class="book-rating">
              <div class="stars">
                <span v-for="i in 5" :key="i" class="star" :class="{ active: i <= book.rating }"
                  >★</span
                >
              </div>
              <span class="rating-text">({{ book.reviews }} đánh giá)</span>
            </div>
            <div class="book-price">
              <span class="current-price">{{ formatPrice(book.price) }}đ</span>
              <span v-if="book.originalPrice" class="original-price"
                >{{ formatPrice(book.originalPrice) }}đ</span
              >
            </div>
            <button class="btn-add-cart">Thêm Vào Giỏ</button>
          </div>
        </div>
      </div>

      <div class="section-footer">
        <button class="btn-view-all">Xem Tất Cả Sách</button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const featuredBooks = ref([
  {
    id: 1,
    title: 'Tôi Tài Giỏi, Bạn Cũng Thế',
    author: 'Adam Khoo',
    price: 89000,
    originalPrice: 120000,
    rating: 5,
    reviews: 234,
    image: 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=300&h=400&fit=crop',
  },
  {
    id: 2,
    title: 'Đắc Nhân Tâm',
    author: 'Dale Carnegie',
    price: 75000,
    originalPrice: 95000,
    rating: 5,
    reviews: 1567,
    image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=300&h=400&fit=crop',
  },
  {
    id: 3,
    title: 'Sapiens: Lược Sử Loài Người',
    author: 'Yuval Noah Harari',
    price: 156000,
    rating: 4,
    reviews: 890,
    image: 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=300&h=400&fit=crop',
  },
  {
    id: 4,
    title: 'Atomic Habits',
    author: 'James Clear',
    price: 142000,
    originalPrice: 168000,
    rating: 5,
    reviews: 445,
    image: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=400&fit=crop',
  },
  {
    id: 5,
    title: 'Nhà Giả Kim',
    author: 'Paulo Coelho',
    price: 68000,
    rating: 4,
    reviews: 2341,
    image: 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=300&h=400&fit=crop',
  },
  {
    id: 6,
    title: 'Thinking, Fast and Slow',
    author: 'Daniel Kahneman',
    price: 198000,
    rating: 4,
    reviews: 156,
    image: 'https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=300&h=400&fit=crop',
  },
])

const formatPrice = (price) => {
  return price.toLocaleString('vi-VN')
}
</script>

<style scoped>
.featured-books {
  padding: 80px 0;
  background: #f8f9fa;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-header {
  text-align: center;
  margin-bottom: 60px;
}

.section-header h2 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 15px;
  font-weight: 700;
}

.section-header p {
  font-size: 1.1rem;
  color: #666;
  max-width: 600px;
  margin: 0 auto;
}

.books-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  margin-bottom: 50px;
}

.book-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.book-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
}

.book-image {
  position: relative;
  height: 300px;
  overflow: hidden;
}

.book-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.book-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.book-card:hover .book-overlay {
  opacity: 1;
}

.book-card:hover .book-image img {
  transform: scale(1.1);
}

.btn-quick-view {
  background: #fff;
  color: #333;
  padding: 10px 20px;
  border: none;
  border-radius: 25px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-quick-view:hover {
  background: #667eea;
  color: white;
}

.book-info {
  padding: 25px;
}

.book-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 8px;
  line-height: 1.3;
}

.book-author {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 12px;
}

.book-rating {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 15px;
}

.stars {
  display: flex;
  gap: 2px;
}

.star {
  color: #ddd;
  font-size: 1.1rem;
}

.star.active {
  color: #ffc107;
}

.rating-text {
  font-size: 0.85rem;
  color: #666;
}

.book-price {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.current-price {
  font-size: 1.3rem;
  font-weight: 700;
  color: #ff6b6b;
}

.original-price {
  font-size: 1rem;
  color: #999;
  text-decoration: line-through;
}

.btn-add-cart {
  width: 100%;
  background: #667eea;
  color: white;
  padding: 12px;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn-add-cart:hover {
  background: #5a67d8;
}

.section-footer {
  text-align: center;
}

.btn-view-all {
  background: transparent;
  color: #667eea;
  padding: 15px 40px;
  border: 2px solid #667eea;
  border-radius: 25px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-view-all:hover {
  background: #667eea;
  color: white;
}

@media (max-width: 768px) {
  .books-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }

  .section-header h2 {
    font-size: 2rem;
  }
}
</style>
