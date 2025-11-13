<script setup>
import { ref } from 'vue'

const text = ref('hello')

const handleInput = (event) => {
  text.value = event.target.value
}
</script>

<template>
  <div>
    <h1>Form Input Binding</h1>
    <input type="text" v-model="text" />
    <p>{{ text }}</p>
  </div>
</template>
