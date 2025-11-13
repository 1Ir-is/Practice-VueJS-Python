<script setup>
import { onMounted, ref } from 'vue'

const inputRef = ref(null)
const list = ['Item 1', 'Item 2', 'Item 3']
const itemRef = ref([])

onMounted(() => {
  inputRef.value.focus()

  itemRef.value.forEach((item) => {
    item.style.transition = 'opacity 5s'
    item.style.opacity = 1
  })
})

const initializeThirdPartyLibrary = (el) => {
  console.log(el)
}

console.log(inputRef)
</script>

<template>
  <div>
    <h1>Template Ref</h1>
    <input type="text" ref="inputRef" />

    <input
      type="text"
      :ref="
        (el) => {
          initializeThirdPartyLibrary(el)
        }
      "
    />

    <ul>
      <li v-for="(item, index) in list" :key="index" ref="itemRef" style="opacity: 0">
        {{ item }}
      </li>
    </ul>
  </div>
</template>
