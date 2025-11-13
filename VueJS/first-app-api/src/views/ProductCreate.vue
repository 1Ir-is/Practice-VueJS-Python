<script setup>
import { createProduct } from '@/service/productService'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

const toast = useToast()
const router = useRouter()
const isSubmitting = ref(false)

const form = ref({
  name: '',
  price: '',
  description: '',
})

const handleSubmit = async () => {
  if (isSubmitting.value) return

  isSubmitting.value = true

  try {
    if (!form.value.name || !form.value.price || !form.value.description) {
      alert('Please fill in all fields')
      return
    }

    const price = parseFloat(form.value.price)
    if (isNaN(price) || price <= 0) {
      alert('Please enter a valid price')
      return
    }

    const productData = {
      name: form.value.name.trim(),
      price: price,
      description: form.value.description.trim(),
    }

    console.log('Creating product:', productData)

    await createProduct(productData)

    form.value = {
      name: '',
      price: '',
      description: '',
    }

    toast.success('Product created successfully!')

    router.push('/products')
  } catch (error) {
    console.error('Error creating product:', error)
    toast.error('Failed to create product. Please try again.')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <div class="create-product">
    <div class="header">
      <h1>Create New Product</h1>
      <p class="subtitle">Fill in the details below to add a new product</p>
    </div>

    <div class="form-container">
      <form @submit.prevent="handleSubmit" class="product-form">
        <div class="form-group">
          <label for="name" class="form-label">Product Name</label>
          <input
            type="text"
            id="name"
            v-model="form.name"
            placeholder="Enter product name"
            class="form-input"
            required
          />
        </div>

        <div class="form-group">
          <label for="price" class="form-label">Price ($)</label>
          <input
            type="number"
            id="price"
            v-model="form.price"
            placeholder="0.00"
            step="0.01"
            min="0"
            class="form-input"
            required
          />
        </div>

        <div class="form-group">
          <label for="description" class="form-label">Description</label>
          <textarea
            id="description"
            v-model="form.description"
            placeholder="Enter product description"
            class="form-textarea"
            rows="4"
            required
          ></textarea>
        </div>

        <div class="form-actions">
          <button
            type="button"
            @click="router.back()"
            class="btn btn-secondary"
            :disabled="isSubmitting"
          >
            Cancel
          </button>
          <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
            <span v-if="!isSubmitting">Create Product</span>
            <span v-else>Creating...</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.create-product {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
}

.header {
  text-align: center;
  margin-bottom: 2rem;
}

.header h1 {
  color: #2c3e50;
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.subtitle {
  color: #7f8c8d;
  font-size: 1.1rem;
  margin: 0;
}

.form-container {
  background: #ffffff;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 1px solid #e1e8ed;
}

.product-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.form-input,
.form-textarea {
  padding: 0.75rem;
  border: 2px solid #e1e8ed;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
  font-family: inherit;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
  justify-content: flex-end;
}

.btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 120px;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-primary {
  background-color: #3498db;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background-color: #2980b9;
  transform: translateY(-1px);
}

.btn-secondary {
  background-color: #95a5a6;
  color: white;
}

.btn-secondary:hover:not(:disabled) {
  background-color: #7f8c8d;
  transform: translateY(-1px);
}

/* Responsive design */
@media (max-width: 768px) {
  .create-product {
    padding: 1rem;
  }

  .form-container {
    padding: 1.5rem;
  }

  .header h1 {
    font-size: 2rem;
  }

  .form-actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }
}
</style>
