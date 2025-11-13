<script setup>
import { ref, watch, watchEffect } from 'vue'

const question = ref('')
const isLoading = ref(false)
const answer = ref('')
const x = ref(0)
const y = ref(0)

watchEffect(() => {
  console.log(`Gia tri cua x: ${x.value}, y: ${y.value}`)
})

watch(question, async (newQuestion, oldQuestion) => {
  if (newQuestion.includes('?')) {
    isLoading.value = true
    answer.value = 'Dang suy nghi'
    try {
      const response = await fetch('https://yesno.wtf/api')
      answer.value = (await response.json()).answer
    } catch (error) {
      ;((answer.value = 'Khong the call api'), error)
    } finally {
      isLoading.value = false
    }
  }
})
</script>

<template>
  <div>
    <h1>Watcher</h1>
    <p>Hoi 1 cau hoi co the tra loi bang yes hoac no</p>
    <input type="text" v-model="question" :disabled="isLoading" />
    <p>{{ answer }}</p>
  </div>
</template>
