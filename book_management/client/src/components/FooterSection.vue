<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <div class="footer-logo">
            <h3>📚 BookStore</h3>
            <p>Nơi khám phá tri thức và lan tỏa văn hóa đọc</p>
          </div>
          <div class="social-links">
            <a href="#" class="social-link">📘</a>
            <a href="#" class="social-link">📱</a>
            <a href="#" class="social-link">📸</a>
            <a href="#" class="social-link">🐦</a>
          </div>
        </div>

        <div class="footer-section">
          <h4>Danh Mục</h4>
          <ul class="footer-links">
            <li><a href="#">Văn học</a></li>
            <li><a href="#">Kinh tế - Kinh doanh</a></li>
            <li><a href="#">Tâm lý - Kỹ năng sống</a></li>
            <li><a href="#">Khoa học - Công nghệ</a></li>
            <li><a href="#">Thiếu nhi</a></li>
          </ul>
        </div>

        <div class="footer-section">
          <h4>Hỗ Trợ</h4>
          <ul class="footer-links">
            <li><a href="#">Liên hệ</a></li>
            <li><a href="#">Hướng dẫn mua hàng</a></li>
            <li><a href="#">Chính sách đổi trả</a></li>
            <li><a href="#">Phương thức thanh toán</a></li>
            <li><a href="#">Câu hỏi thường gặp</a></li>
          </ul>
        </div>

        <div class="footer-section">
          <h4>Thông Tin Liên Hệ</h4>
          <div class="contact-info">
            <div class="contact-item">
              <span class="contact-icon">📍</span>
              <span>123 Đường ABC, Quận XYZ, TP.HCM</span>
            </div>
            <div class="contact-item">
              <span class="contact-icon">📞</span>
              <span>1900 1234</span>
            </div>
            <div class="contact-item">
              <span class="contact-icon">📧</span>
              <span>info@bookstore.vn</span>
            </div>
            <div class="contact-item">
              <span class="contact-icon">🕒</span>
              <span>8:00 - 22:00 (Thứ 2 - CN)</span>
            </div>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="footer-bottom-content">
          <p>&copy; 2024 BookStore. Tất cả quyền được bảo lưu.</p>
          <div class="footer-bottom-links">
            <a href="#">Điều khoản sử dụng</a>
            <a href="#">Chính sách bảo mật</a>
            <a href="#">Cookie</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: #2d3748;
  color: white;
  padding: 60px 0 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-content {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 40px;
  margin-bottom: 40px;
}

.footer-section h4 {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 20px;
  color: #e2e8f0;
}

.footer-logo h3 {
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 15px;
  color: #667eea;
}

.footer-logo p {
  color: #a0aec0;
  line-height: 1.6;
  margin-bottom: 25px;
}

.social-links {
  display: flex;
  gap: 15px;
}

.social-link {
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  font-size: 1.2rem;
  transition: all 0.3s ease;
}

.social-link:hover {
  background: #667eea;
  transform: translateY(-2px);
}

.footer-links {
  list-style: none;
  padding: 0;
}

.footer-links li {
  margin-bottom: 12px;
}

.footer-links a {
  color: #a0aec0;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-links a:hover {
  color: #667eea;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #a0aec0;
  font-size: 0.95rem;
}

.contact-icon {
  font-size: 1.1rem;
}

.footer-bottom {
  border-top: 1px solid #4a5568;
  padding: 25px 0;
}

.footer-bottom-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #a0aec0;
  font-size: 0.9rem;
}

.footer-bottom-links {
  display: flex;
  gap: 25px;
}

.footer-bottom-links a {
  color: #a0aec0;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-bottom-links a:hover {
  color: #667eea;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 30px;
    text-align: center;
  }

  .footer-bottom-content {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }

  .footer-bottom-links {
    justify-content: center;
  }

  .social-links {
    justify-content: center;
  }
}
</style>
