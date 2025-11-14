<template>
  <section class="categories">
    <div class="container">
      <div class="section-header">
        <h2>Danh Mục Sách</h2>
        <p>Khám phá thế giới kiến thức qua các danh mục đa dạng</p>
      </div>

      <div class="categories-grid">
        <div class="category-card" v-for="category in categories" :key="category.id">
          <div class="category-icon">
            <i :class="category.icon"></i>
          </div>
          <h3 class="category-title">{{ category.name }}</h3>
          <p class="category-description">{{ category.description }}</p>
          <div class="category-stats">
            <span class="book-count">{{ category.bookCount }} cuốn sách</span>
          </div>
          <div class="category-overlay">
            <button class="btn-explore">Khám Phá</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const categories = ref([
  {
    id: 1,
    name: 'Văn Học',
    description: 'Tiểu thuyết, thơ ca, văn học kinh điển từ trong nước và quốc tế',
    bookCount: 2850,
    icon: '📚',
  },
  {
    id: 2,
    name: 'Kinh Tế - Kinh Doanh',
    description: 'Sách về quản lý, khởi nghiệp, đầu tư và phát triển doanh nghiệp',
    bookCount: 1650,
    icon: '💼',
  },
  {
    id: 3,
    name: 'Tâm Lý - Kỹ Năng Sống',
    description: 'Phát triển bản thân, tâm lý học và các kỹ năng sống',
    bookCount: 1240,
    icon: '🧠',
  },
  {
    id: 4,
    name: 'Khoa Học - Công Nghệ',
    description: 'Khám phá khoa học, công nghệ và những phát minh mới',
    bookCount: 980,
    icon: '🔬',
  },
  {
    id: 5,
    name: 'Lịch Sử - Địa Lý',
    description: 'Tìm hiểu về quá khứ và những vùng đất trên thế giới',
    bookCount: 756,
    icon: '🌍',
  },
  {
    id: 6,
    name: 'Thiếu Nhi',
    description: 'Sách tranh, truyện cổ tích và sách giáo dục cho trẻ em',
    bookCount: 1890,
    icon: '🎈',
  },
  {
    id: 7,
    name: 'Y Học - Sức Khỏe',
    description: 'Chăm sóc sức khỏe, y học và lối sống lành mạnh',
    bookCount: 567,
    icon: '🏥',
  },
  {
    id: 8,
    name: 'Ngoại Ngữ',
    description: 'Học tiếng Anh, tiếng Nhật, tiếng Hàn và các ngoại ngữ khác',
    bookCount: 834,
    icon: '🗣️',
  },
])
</script>

<style scoped>
.categories {
  padding: 80px 0;
  background: white;
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

.categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
}

.category-card {
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 15px;
  padding: 30px 25px;
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
}

.category-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.category-card:hover::before {
  left: 100%;
}

.category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  border-color: #667eea;
}

.category-icon {
  font-size: 3rem;
  margin-bottom: 20px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.category-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 12px;
}

.category-description {
  color: #666;
  line-height: 1.5;
  margin-bottom: 20px;
  font-size: 0.95rem;
}

.category-stats {
  margin-bottom: 20px;
}

.book-count {
  background: #f1f5f9;
  color: #64748b;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
}

.category-overlay {
  position: absolute;
  bottom: -60px;
  left: 0;
  right: 0;
  padding: 20px;
  transition: bottom 0.3s ease;
}

.category-card:hover .category-overlay {
  bottom: 0;
}

.btn-explore {
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

.btn-explore:hover {
  background: #5a67d8;
}

@media (max-width: 768px) {
  .categories-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }

  .section-header h2 {
    font-size: 2rem;
  }

  .category-card {
    padding: 25px 20px;
  }

  .category-overlay {
    position: static;
    padding: 0;
    margin-top: 15px;
  }
}
</style>
