<script setup>
import { ref, reactive, nextTick } from 'vue'

const count = ref(0)

const increase = async () => {
  count.value++
  await nextTick()
  console.log(document.getElementById('count').innerText)
}

const object = reactive({
  count: 2,
  user: {
    age: 15,
  },
  array: [1, 2, 3],
})

const change = () => {
  object.count++
  object.user.age++
  object.array.push(4)
}
</script>

<template>
  <div>
    <!-- <p>Count: {{ object.count }}</p>
    <p>Age: {{ object.user.age }}</p>
    <p>Array: {{ object.array }}</p>
    <button @click="change">Increase</button> -->

    <p id="count">Count: {{ count }}</p>
    <button @click="increase">Click</button>
  </div>
</template>
