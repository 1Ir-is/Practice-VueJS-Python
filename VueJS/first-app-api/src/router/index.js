import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductList from '@/views/ProductList.vue'
import ProductDetail from '@/views/ProductDetail.vue'
import ProductCreate from '@/views/ProductCreate.vue'
import ProductEdit from '@/views/ProductEdit.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: { guestOnly: true },
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
    meta: { guestOnly: true },
  },
  {
    path: '/products',
    name: 'products',
    component: ProductList,
    meta: { requiresAuth: true },
  },
  {
    path: '/products/create',
    name: 'product-create',
    component: ProductCreate,
    meta: { requiresAuth: true },
  },
  {
    path: '/products/:id',
    name: 'product-detail',
    component: ProductDetail,
    meta: { requiresAuth: true },
  },
  {
    path: '/products/:id/edit',
    name: 'product-edit',
    component: ProductEdit,
    meta: { requiresAuth: true },
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

function isLoggedIn() {
  return !!(localStorage.getItem('access_token') || sessionStorage.getItem('access_token'))
}

router.beforeEach((to, from, next) => {
  const loggedIn = isLoggedIn()

  if (to.meta?.guestOnly && loggedIn) {
    return next({ name: 'products' })
  }

  if (to.meta?.requiresAuth && !loggedIn) {
    return next({ name: 'login', query: { next: to.fullPath } })
  }
  return next()
})

export default router
