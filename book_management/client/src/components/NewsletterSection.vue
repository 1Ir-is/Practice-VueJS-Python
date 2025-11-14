<template>
  <section class="newsletter">
    <div class="container">
      <div class="newsletter-content">
        <div class="newsletter-text">
          <h2>Đừng Bỏ Lỡ Sách Mới</h2>
          <p>
            Đăng ký nhận tin tức để được thông báo về sách mới, chương trình khuyến mãi và những
            cuốn sách được giới thiệu đặc biệt từ chúng tôi.
          </p>
          <div class="newsletter-benefits">
            <div class="benefit">
              <span class="benefit-icon">📚</span>
              <span>Thông báo sách mới hàng tuần</span>
            </div>
            <div class="benefit">
              <span class="benefit-icon">🎯</span>
              <span>Khuyến mãi độc quyền cho thành viên</span>
            </div>
            <div class="benefit">
              <span class="benefit-icon">⭐</span>
              <span>Review sách từ chuyên gia</span>
            </div>
          </div>
        </div>

        <div class="newsletter-form">
          <form @submit.prevent="subscribe">
            <div class="form-group">
              <input
                type="text"
                v-model="form.name"
                placeholder="Họ và tên"
                class="form-input"
                required
              />
            </div>
            <div class="form-group">
              <input
                type="email"
                v-model="form.email"
                placeholder="Email của bạn"
                class="form-input"
                required
              />
            </div>
            <div class="form-group">
              <select v-model="form.category" class="form-select">
                <option value="">Danh mục quan tâm</option>
                <option value="literature">Văn học</option>
                <option value="business">Kinh tế - Kinh doanh</option>
                <option value="psychology">Tâm lý - Kỹ năng sống</option>
                <option value="science">Khoa học - Công nghệ</option>
                <option value="history">Lịch sử - Địa lý</option>
                <option value="children">Thiếu nhi</option>
                <option value="health">Y học - Sức khỏe</option>
                <option value="language">Ngoại ngữ</option>
              </select>
            </div>
            <button type="submit" class="btn-subscribe" :disabled="isSubmitting">
              <span v-if="isSubmitting">Đang đăng ký...</span>
              <span v-else>Đăng Ký Ngay</span>
            </button>
          </form>

          <p class="privacy-note">
            🔒 Chúng tôi tôn trọng quyền riêng tư của bạn. Không spam, có thể hủy đăng ký bất cứ lúc
            nào.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from 'vue'

const isSubmitting = ref(false)

const form = reactive({
  name: '',
  email: '',
  category: '',
})

const subscribe = async () => {
  isSubmitting.value = true

  // Simulate API call
  try {
    await new Promise((resolve) => setTimeout(resolve, 1500))

    // Reset form
    form.name = ''
    form.email = ''
    form.category = ''

    alert('Đăng ký thành công! Chúng tôi sẽ gửi tin tức sách mới đến email của bạn.')
  } catch {
    alert('Có lỗi xảy ra. Vui lòng thử lại sau.')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
.newsletter {
  padding: 80px 0;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.newsletter-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.newsletter-text h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 20px;
  line-height: 1.2;
}

.newsletter-text p {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 30px;
  opacity: 0.9;
}

.newsletter-benefits {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.benefit {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1rem;
}

.benefit-icon {
  font-size: 1.2rem;
}

.newsletter-form {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  padding: 40px;
}

.form-group {
  margin-bottom: 20px;
}

.form-input,
.form-select {
  width: 100%;
  padding: 15px 20px;
  border: none;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.9);
  font-size: 1rem;
  transition: all 0.3s ease;
}

.form-input:focus,
.form-select:focus {
  outline: none;
  background: white;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.3);
}

.form-input::placeholder {
  color: #666;
}

.btn-subscribe {
  width: 100%;
  background: white;
  color: #f5576c;
  padding: 15px;
  border: none;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-bottom: 20px;
}

.btn-subscribe:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.btn-subscribe:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.privacy-note {
  font-size: 0.9rem;
  text-align: center;
  opacity: 0.8;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .newsletter-content {
    grid-template-columns: 1fr;
    gap: 40px;
    text-align: center;
  }

  .newsletter-text h2 {
    font-size: 2rem;
  }

  .newsletter-form {
    padding: 30px;
  }

  .newsletter-benefits {
    justify-content: center;
    align-items: center;
  }
}
</style>
