<script setup>
import { RouterView } from 'vue-router'
import FooterSection from './components/FooterSection.vue'
</script>

<template>
  <div id="app">
    <header class="main-header">
      <nav class="navbar">
        <div class="nav-container">
          <div class="nav-brand">
            <h1>📚 BookStore</h1>
          </div>
          <div class="nav-menu">
            <a href="#" class="nav-link">Trang chủ</a>
            <a href="#" class="nav-link">Danh mục</a>
            <a href="#" class="nav-link">Bestsellers</a>
            <a href="#" class="nav-link">Khuyến mãi</a>
            <a href="#" class="nav-link">Về chúng tôi</a>
          </div>
          <div class="nav-actions">
            <button class="nav-btn search-btn">🔍</button>
            <button class="nav-btn cart-btn">
              🛒
              <span class="cart-badge">3</span>
            </button>
            <button class="nav-btn user-btn">👤</button>
          </div>
        </div>
      </nav>
    </header>

    <RouterView />

    <FooterSection />
  </div>
</template>

<style scoped>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-header {
  background: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.navbar {
  padding: 0;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 15px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-brand h1 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #667eea;
  margin: 0;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 30px;
}

.nav-link {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.nav-link:hover {
  color: #667eea;
  background: #f8f9fa;
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 15px;
}

.nav-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background: #f8f9fa;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  transition: all 0.3s ease;
  position: relative;
}

.nav-btn:hover {
  background: #667eea;
  color: white;
}

.cart-badge {
  position: absolute;
  top: -5px;
  right: -5px;
  background: #ff6b6b;
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

main {
  flex: 1;
  margin-top: 70px; /* Account for fixed header */
}

@media (max-width: 768px) {
  .nav-menu {
    display: none;
  }

  .nav-container {
    padding: 12px 20px;
  }

  .nav-brand h1 {
    font-size: 1.5rem;
  }

  .nav-actions {
    gap: 10px;
  }

  .nav-btn {
    width: 36px;
    height: 36px;
    font-size: 1.1rem;
  }
}
</style>

<style>
/* Global styles */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: #333;
}

button {
  font-family: inherit;
}

a {
  color: inherit;
}
</style>
