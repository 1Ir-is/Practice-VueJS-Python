<script setup>
import { ref } from 'vue'

const count = ref(0)

const sayHi = (name) => {
  alert(`Xin chao ${name}`)
}

const submit = () => {
  alert('Submit')
}
</script>

<template>
  <div>
    <button @click.stop="sayHi('A')">Chao A</button>
    <form @submit.prevent="submit">
      <button type="submit">Submit</button>
    </form>

    <input type="text" @keyup.enter="submit" />
  </div>
</template>
