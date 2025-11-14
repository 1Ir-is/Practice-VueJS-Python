<template>
  <section class="hero">
    <div class="hero-content">
      <div class="hero-text">
        <h1 class="hero-title">Khám Phá Thế Giới Sách</h1>
        <p class="hero-subtitle">
          Hàng ngàn cuốn sách hay đang chờ bạn khám phá. Từ tiểu thuyết đến sách khoa học, chúng tôi
          có tất cả những gì bạn cần.
        </p>
        <div class="hero-buttons">
          <button class="btn btn-primary">Mua Sách Ngay</button>
          <button class="btn btn-outline">Xem Catalog</button>
        </div>
        <div class="hero-stats">
          <div class="stat">
            <span class="stat-number">10,000+</span>
            <span class="stat-label">Đầu sách</span>
          </div>
          <div class="stat">
            <span class="stat-number">50,000+</span>
            <span class="stat-label">Khách hàng</span>
          </div>
          <div class="stat">
            <span class="stat-number">4.8★</span>
            <span class="stat-label">Đánh giá</span>
          </div>
        </div>
      </div>
      <div class="hero-image">
        <div class="book-stack">
          <div class="book book-1">
            <div class="book-cover">
              <h3>Văn Học</h3>
            </div>
          </div>
          <div class="book book-2">
            <div class="book-cover">
              <h3>Khoa Học</h3>
            </div>
          </div>
          <div class="book book-3">
            <div class="book-cover">
              <h3>Kinh Tế</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 80px 0;
  min-height: 100vh;
  display: flex;
  align-items: center;
}

.hero-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 20px;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.2rem;
  margin-bottom: 30px;
  line-height: 1.6;
  opacity: 0.9;
}

.hero-buttons {
  display: flex;
  gap: 15px;
  margin-bottom: 40px;
}

.btn {
  padding: 15px 30px;
  border-radius: 50px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
}

.btn-primary {
  background: #ff6b6b;
  color: white;
}

.btn-primary:hover {
  background: #ff5252;
  transform: translateY(-2px);
}

.btn-outline {
  background: transparent;
  color: white;
  border: 2px solid white;
}

.btn-outline:hover {
  background: white;
  color: #667eea;
}

.hero-stats {
  display: flex;
  gap: 40px;
}

.stat {
  text-align: center;
}

.stat-number {
  display: block;
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 0.9rem;
  opacity: 0.8;
}

.hero-image {
  display: flex;
  justify-content: center;
  align-items: center;
}

.book-stack {
  position: relative;
  transform: perspective(1000px) rotateY(-15deg);
}

.book {
  width: 180px;
  height: 250px;
  position: relative;
  margin-bottom: 10px;
  transform-style: preserve-3d;
  transition: transform 0.3s ease;
}

.book:hover {
  transform: translateZ(20px) rotateY(5deg);
}

.book-cover {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1.1rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.book-1 .book-cover {
  background: linear-gradient(135deg, #4ecdc4, #44a08d);
}

.book-2 .book-cover {
  background: linear-gradient(135deg, #f093fb, #f5576c);
  transform: translateX(-20px) translateZ(-10px);
}

.book-3 .book-cover {
  background: linear-gradient(135deg, #4facfe, #00f2fe);
  transform: translateX(-40px) translateZ(-20px);
}

@media (max-width: 768px) {
  .hero-content {
    grid-template-columns: 1fr;
    gap: 40px;
    text-align: center;
  }

  .hero-title {
    font-size: 2.5rem;
  }

  .hero-buttons {
    justify-content: center;
  }

  .hero-stats {
    justify-content: center;
  }

  .book-stack {
    transform: perspective(1000px) rotateY(0deg);
    scale: 0.8;
  }
}
</style>
