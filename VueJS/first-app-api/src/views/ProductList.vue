<script setup>
import { deleteProduct, getProducts } from '@/service/productService'
import { onMounted, ref } from 'vue'
import { useToast } from 'vue-toastification'

const toast = useToast()
const products = ref([])
const loading = ref(true)
const error = ref('')

const fetchProducts = async () => {
  loading.value = true
  error.value = ''
  try {
    const response = await getProducts()
    products.value = response.data
  } catch (err) {
    error.value = 'Failed to fetch products.'
    console.error('Error fetching products:', err)
  } finally {
    loading.value = false
  }
}

const removeProduct = async (id, productName) => {
  if (confirm(`Are you sure you want to delete "${productName}"?`)) {
    try {
      await deleteProduct(id)
      toast.success('Product deleted successfully!')
      await fetchProducts()
    } catch (err) {
      toast.error('Failed to delete product. Please try again.')
      console.error('Error deleting product:', err)
    }
  }
}

const formatPrice = (price) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(price)
}

onMounted(() => {
  fetchProducts()
})
</script>

<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div
      class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 pb-6 border-b-2 border-gray-200"
    >
      <div class="mb-4 sm:mb-0">
        <h1 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-2">Product Management</h1>
        <p class="text-gray-600 text-lg">Manage your product inventory</p>
      </div>
      <router-link
        to="/products/create"
        class="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 4v16m8-8H4"
          ></path>
        </svg>
        Add Product
      </router-link>
    </div>

    <div v-if="loading" class="flex flex-col items-center justify-center py-16">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
      <p class="text-gray-600 text-lg">Loading products...</p>
    </div>

    <div v-else-if="error" class="bg-red-50 border-2 border-red-200 rounded-xl p-6 text-center">
      <div class="flex flex-col items-center space-y-4">
        <svg class="w-12 h-12 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"
          ></path>
        </svg>
        <p class="text-red-700 font-medium text-lg">{{ error }}</p>
        <button
          @click="fetchProducts"
          class="bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200"
        >
          Try Again
        </button>
      </div>
    </div>

    <div v-else-if="products.length === 0" class="text-center py-16">
      <svg
        class="w-24 h-24 text-gray-300 mx-auto mb-6"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"
        ></path>
      </svg>
      <h3 class="text-2xl font-bold text-gray-900 mb-2">No products found</h3>
      <p class="text-gray-600 text-lg mb-6">Get started by adding your first product</p>
      <router-link
        to="/products/create"
        class="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200"
      >
        Add Your First Product
      </router-link>
    </div>

    <div v-else>
      <div class="bg-gray-50 rounded-lg p-4 mb-6">
        <p class="text-gray-600 font-medium">
          {{ products.length }} product{{ products.length !== 1 ? 's' : '' }} found
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="product in products"
          :key="product.id"
          class="bg-white rounded-xl shadow-md hover:shadow-xl border border-gray-200 overflow-hidden transform hover:-translate-y-1 transition-all duration-300"
        >
          <div class="p-6 pb-4">
            <div class="flex justify-between items-start mb-3">
              <h3 class="text-xl font-bold text-gray-900 flex-1 mr-4 leading-tight">
                {{ product.name }}
              </h3>
              <span
                class="bg-green-500 text-white px-3 py-1 rounded-full text-sm font-bold whitespace-nowrap"
              >
                {{ formatPrice(product.price) }}
              </span>
            </div>

            <div class="mb-6">
              <p class="text-gray-600 line-clamp-3 leading-relaxed">
                {{ product.description }}
              </p>
            </div>
          </div>

          <div class="px-6 pb-6">
            <div class="flex flex-col sm:flex-row gap-2">
              <router-link
                :to="`/products/${product.id}`"
                class="flex-1 inline-flex items-center justify-center gap-2 bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium py-2 px-3 rounded-lg transition-colors duration-200 text-sm"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  ></path>
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                  ></path>
                </svg>
                View
              </router-link>

              <router-link
                :to="`/products/${product.id}/edit`"
                class="flex-1 inline-flex items-center justify-center gap-2 bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-3 rounded-lg transition-colors duration-200 text-sm"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
                  ></path>
                </svg>
                Edit
              </router-link>

              <button
                @click="removeProduct(product.id, product.name)"
                class="flex-1 inline-flex items-center justify-center gap-2 bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-3 rounded-lg transition-colors duration-200 text-sm"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                  ></path>
                </svg>
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
