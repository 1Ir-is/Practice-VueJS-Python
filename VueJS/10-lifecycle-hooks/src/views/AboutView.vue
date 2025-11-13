<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h1 id="count">Count: {{ count }}</h1>
    <button @click="increment">increment</button>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<script setup>
import { onBeforeMount, onBeforeUnmount, onBeforeUpdate, onMounted, onUnmounted, onUpdated, ref } from 'vue';
const count = ref(0)

const increment = () => {
  count.value++
}

onBeforeUpdate(() => {
  console.log("Onbeforeupdate", document.getElementById("count").textContent)
})

onUpdated(() => {
  console.log("Onupdated", document.getElementById("count").textContent)
})




</script>
