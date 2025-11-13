<script setup>
import { getProduct } from '@/service/productService'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const product = ref(null)
const route = useRoute()
const router = useRouter()
const error = ref('')
const loading = ref(true)

const formatPrice = (price) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(price)
}

const goBack = () => {
  router.push('/products')
}

onMounted(async () => {
  loading.value = true
  try {
    const response = await getProduct(route.params.id)
    product.value = response.data
    error.value = ''
  } catch (err) {
    error.value = 'Failed to fetch product details.'
    console.error('Failed to fetch product details.', err)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="mb-8">
      <div class="flex items-center gap-4 mb-4">
        <button
          @click="goBack"
          class="inline-flex items-center text-gray-600 hover:text-gray-900 transition-colors duration-200"
        >
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M10 19l-7-7m0 0l7-7m-7 7h18"
            ></path>
          </svg>
          Back to Products
        </button>
      </div>
      <h1 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-2">Product Details</h1>
      <p class="text-gray-600 text-lg">View detailed product information</p>
    </div>

    <div v-if="loading" class="flex flex-col items-center justify-center py-16">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
      <p class="text-gray-600 text-lg">Loading product details...</p>
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
        <div class="flex gap-4">
          <button
            @click="$router.go(0)"
            class="bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200"
          >
            Try Again
          </button>
          <button
            @click="goBack"
            class="bg-gray-600 hover:bg-gray-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200"
          >
            Go Back
          </button>
        </div>
      </div>
    </div>

    <div v-else-if="product" class="space-y-6">
      <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
        <div class="px-8 py-6 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-gray-200">
          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
            <div>
              <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 mb-2">{{ product.name }}</h2>
              <div class="flex items-center gap-2">
                <span class="bg-green-500 text-white px-3 py-1 rounded-full text-lg font-bold">
                  {{ formatPrice(product.price) }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <div class="p-8">
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div class="lg:col-span-2">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                <svg
                  class="w-5 h-5 mr-2 text-blue-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                  ></path>
                </svg>
                Description
              </h3>
              <div class="bg-gray-50 rounded-lg p-4">
                <p class="text-gray-700 leading-relaxed">{{ product.description }}</p>
              </div>
            </div>

            <div class="space-y-4">
              <div
                class="bg-gradient-to-br from-green-50 to-green-100 rounded-lg p-4 border border-green-200"
              >
                <div class="flex items-center justify-between">
                  <div>
                    <p class="text-green-700 text-sm font-medium">Price</p>
                    <p class="text-2xl font-bold text-green-900">
                      {{ formatPrice(product.price) }}
                    </p>
                  </div>
                  <div class="bg-green-500 p-3 rounded-full">
                    <svg
                      class="w-6 h-6 text-white"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"
                      ></path>
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Actions</h3>
        <div class="flex flex-col sm:flex-row gap-4">
          <router-link
            :to="`/products/${product.id}/edit`"
            class="flex-1 inline-flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
              ></path>
            </svg>
            Edit Product
          </router-link>

          <button
            @click="goBack"
            class="flex-1 inline-flex items-center justify-center gap-2 bg-gray-500 hover:bg-gray-600 text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              ></path>
            </svg>
            Back to List
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
