<template>
  <section class="testimonials">
    <div class="container">
      <div class="section-header">
        <h2>Khách Hàng Nói Gì</h2>
        <p>Hàng nghìn khách hàng đã tin tưởng và hài lòng với dịch vụ của chúng tôi</p>
      </div>

      <div class="testimonials-slider">
        <div
          class="testimonials-track"
          :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
        >
          <div class="testimonial-slide" v-for="testimonial in testimonials" :key="testimonial.id">
            <div class="testimonial-card">
              <div class="quote-icon">❝</div>
              <p class="testimonial-text">{{ testimonial.text }}</p>
              <div class="testimonial-rating">
                <div class="stars">
                  <span
                    v-for="i in 5"
                    :key="i"
                    class="star"
                    :class="{ active: i <= testimonial.rating }"
                    >★</span
                  >
                </div>
              </div>
              <div class="testimonial-author">
                <div class="author-avatar">
                  <img :src="testimonial.avatar" :alt="testimonial.name" />
                </div>
                <div class="author-info">
                  <h4 class="author-name">{{ testimonial.name }}</h4>
                  <p class="author-title">{{ testimonial.title }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="slider-controls">
          <button class="slider-btn prev" @click="previousSlide" :disabled="currentSlide === 0">
            ‹
          </button>
          <div class="slider-dots">
            <button
              v-for="(_, index) in Math.ceil(testimonials.length / 3)"
              :key="index"
              class="dot"
              :class="{ active: index === currentSlide }"
              @click="goToSlide(index)"
            ></button>
          </div>
          <button
            class="slider-btn next"
            @click="nextSlide"
            :disabled="currentSlide === Math.ceil(testimonials.length / 3) - 1"
          >
            ›
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const currentSlide = ref(0)
const autoSlideInterval = ref(null)

const testimonials = ref([
  {
    id: 1,
    text: 'Cửa hàng sách tuyệt vời! Tôi đã tìm thấy những cuốn sách hay mà tôi tìm kiếm từ lâu. Dịch vụ giao hàng nhanh và đóng gói cẩn thận.',
    name: 'Nguyễn Thị Mai',
    title: 'Giáo viên',
    rating: 5,
    avatar:
      'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=100&h=100&fit=crop&crop=face',
  },
  {
    id: 2,
    text: 'Giá cả hợp lý, chất lượng sách tốt. Đặc biệt thích phần sách thiếu nhi cho con tôi. Sẽ tiếp tục ủng hộ cửa hàng!',
    name: 'Lê Văn Hùng',
    title: 'Kỹ sư',
    rating: 5,
    avatar:
      'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face',
  },
  {
    id: 3,
    text: 'Website dễ sử dụng, tìm kiếm sách rất tiện lợi. Đội ngũ tư vấn nhiệt tình và am hiểu về sách. Highly recommended!',
    name: 'Trần Minh Châu',
    title: 'Designer',
    rating: 5,
    avatar:
      'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop&crop=face',
  },
  {
    id: 4,
    text: 'Mua sách để nghiên cứu luận văn, có rất nhiều đầu sách chuyên ngành. Giao hàng đúng hẹn và sách đều còn mới 100%.',
    name: 'Phạm Quốc Anh',
    title: 'Sinh viên',
    rating: 4,
    avatar:
      'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop&crop=face',
  },
  {
    id: 5,
    text: 'Chương trình khuyến mãi thường xuyên, giá tốt. Đã mua hàng trăm cuốn sách ở đây và chưa bao giờ thất vọng.',
    name: 'Vũ Thị Lan',
    title: 'Nhân viên văn phòng',
    rating: 5,
    avatar:
      'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=100&h=100&fit=crop&crop=face',
  },
  {
    id: 6,
    text: 'Dịch vụ khách hàng xuất sắc! Khi có vấn đề với đơn hàng, được giải quyết rất nhanh chóng và hài lòng.',
    name: 'Hoàng Minh Tuấn',
    title: 'Doanh nhân',
    rating: 5,
    avatar:
      'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop&crop=face',
  },
])

const maxSlides = Math.ceil(testimonials.value.length / 3)

const nextSlide = () => {
  if (currentSlide.value < maxSlides - 1) {
    currentSlide.value++
  } else {
    currentSlide.value = 0
  }
}

const previousSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value--
  } else {
    currentSlide.value = maxSlides - 1
  }
}

const goToSlide = (index) => {
  currentSlide.value = index
}

const startAutoSlide = () => {
  autoSlideInterval.value = setInterval(nextSlide, 5000)
}

const stopAutoSlide = () => {
  if (autoSlideInterval.value) {
    clearInterval(autoSlideInterval.value)
  }
}

onMounted(() => {
  startAutoSlide()
})

onUnmounted(() => {
  stopAutoSlide()
})
</script>

<style scoped>
.testimonials {
  padding: 80px 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
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
  margin-bottom: 15px;
  font-weight: 700;
}

.section-header p {
  font-size: 1.1rem;
  opacity: 0.9;
  max-width: 600px;
  margin: 0 auto;
}

.testimonials-slider {
  position: relative;
  overflow: hidden;
}

.testimonials-track {
  display: flex;
  transition: transform 0.5s ease;
}

.testimonial-slide {
  min-width: 100%;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
  padding: 0 10px;
}

.testimonial-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  padding: 30px;
  text-align: center;
  transition: transform 0.3s ease;
}

.testimonial-card:hover {
  transform: translateY(-5px);
}

.quote-icon {
  font-size: 3rem;
  opacity: 0.3;
  margin-bottom: 20px;
}

.testimonial-text {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 25px;
  font-style: italic;
}

.testimonial-rating {
  margin-bottom: 25px;
}

.stars {
  display: flex;
  justify-content: center;
  gap: 2px;
}

.star {
  color: rgba(255, 255, 255, 0.3);
  font-size: 1.2rem;
}

.star.active {
  color: #ffc107;
}

.testimonial-author {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
}

.author-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.author-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.author-info {
  text-align: left;
}

.author-name {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 5px;
}

.author-title {
  font-size: 0.9rem;
  opacity: 0.8;
}

.slider-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  margin-top: 40px;
}

.slider-btn {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 2px solid rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.1);
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.slider-btn:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.5);
}

.slider-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.slider-dots {
  display: flex;
  gap: 10px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: none;
  background: rgba(255, 255, 255, 0.3);
  cursor: pointer;
  transition: background 0.3s ease;
}

.dot.active {
  background: white;
}

@media (max-width: 768px) {
  .testimonial-slide {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .testimonial-card {
    padding: 25px;
  }

  .section-header h2 {
    font-size: 2rem;
  }

  .slider-controls {
    flex-direction: column;
    gap: 15px;
  }
}
</style>
