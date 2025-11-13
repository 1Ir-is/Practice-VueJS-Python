<script setup>
import { getProduct, updateProduct } from '@/service/productService'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

const toast = useToast()
const router = useRouter()
const route = useRoute()
const error = ref('')
const loading = ref(true)
const isSubmitting = ref(false)
const form = ref({
  name: '',
  price: '',
  description: '',
})

onMounted(async () => {
  try {
    const response = await getProduct(route.params.id)
    form.value = response.data
    error.value = ''
  } catch (err) {
    error.value = 'Failed to fetch product details.'
    console.error('Error fetching product:', err)
  } finally {
    loading.value = false
  }
})

const handleEdit = async () => {
  if (isSubmitting.value) return

  if (!form.value.name || !form.value.price || !form.value.description) {
    error.value = 'Please fill in all fields'
    return
  }

  const price = parseFloat(form.value.price)
  if (isNaN(price) || price <= 0) {
    error.value = 'Please enter a valid price'
    return
  }

  isSubmitting.value = true
  error.value = ''

  try {
    const productData = {
      name: form.value.name.trim(),
      price: price,
      description: form.value.description.trim(),
    }

    await updateProduct(route.params.id, productData)
    toast.success('Product updated successfully!')
    router.push('/products')
  } catch (err) {
    error.value = 'Failed to update product. Please try again.'
    console.error('Error updating product:', err)
  } finally {
    isSubmitting.value = false
  }
}

const handleCancel = () => {
  router.push('/products')
}
</script>

<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="mb-8">
      <div class="flex items-center gap-4 mb-4">
        <button
          @click="handleCancel"
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
      <h1 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-2">Edit Product</h1>
      <p class="text-gray-600 text-lg">Update product information</p>
    </div>

    <div v-if="loading" class="flex flex-col items-center justify-center py-16">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
      <p class="text-gray-600 text-lg">Loading product details...</p>
    </div>

    <div
      v-else-if="error && !form.name"
      class="bg-red-50 border-2 border-red-200 rounded-xl p-6 text-center"
    >
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
            @click="handleCancel"
            class="bg-gray-600 hover:bg-gray-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200"
          >
            Go Back
          </button>
        </div>
      </div>
    </div>

    <div v-else class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
      <div class="p-8">
        <div
          v-if="error"
          class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-6 flex items-center"
        >
          <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"
            ></path>
          </svg>
          {{ error }}
        </div>

        <form @submit.prevent="handleEdit" class="space-y-6">
          <div>
            <label for="name" class="block text-sm font-semibold text-gray-700 mb-2">
              Product Name
            </label>
            <input
              id="name"
              v-model="form.name"
              type="text"
              placeholder="Enter product name"
              required
              :disabled="isSubmitting"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:outline-none transition-colors duration-200 disabled:bg-gray-100 disabled:cursor-not-allowed"
            />
          </div>

          <div>
            <label for="price" class="block text-sm font-semibold text-gray-700 mb-2">
              Price ($)
            </label>
            <input
              id="price"
              v-model="form.price"
              type="number"
              step="0.01"
              min="0"
              placeholder="0.00"
              required
              :disabled="isSubmitting"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:outline-none transition-colors duration-200 disabled:bg-gray-100 disabled:cursor-not-allowed"
            />
          </div>
          <div>
            <label for="description" class="block text-sm font-semibold text-gray-700 mb-2">
              Description
            </label>
            <textarea
              id="description"
              v-model="form.description"
              rows="4"
              placeholder="Enter product description"
              required
              :disabled="isSubmitting"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:outline-none transition-colors duration-200 resize-vertical disabled:bg-gray-100 disabled:cursor-not-allowed"
            ></textarea>
          </div>
          <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
            <button
              type="submit"
              :disabled="isSubmitting"
              class="flex-1 inline-flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400 text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200 disabled:transform-none disabled:cursor-not-allowed"
            >
              <svg
                v-if="isSubmitting"
                class="animate-spin w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
                ></path>
              </svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 13l4 4L19 7"
                ></path>
              </svg>
              {{ isSubmitting ? 'Updating...' : 'Update Product' }}
            </button>

            <button
              type="button"
              @click="handleCancel"
              :disabled="isSubmitting"
              class="flex-1 inline-flex items-center justify-center gap-2 bg-gray-500 hover:bg-gray-600 disabled:bg-gray-300 text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200 disabled:transform-none disabled:cursor-not-allowed"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                ></path>
              </svg>
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
