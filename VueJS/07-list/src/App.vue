<script setup>
import { ref } from 'vue'
import List from './ListItem.vue'

const shoppingList = ref([
  { id: 1, name: 'Apples', quantity: 5 },
  { id: 2, name: 'Bananas', quantity: 3 },
  { id: 3, name: 'Carrots', quantity: 4 },
])
</script>

<template>
  <div>
    <h1>Shopping List</h1>
    <ul>
      <List v-for="item in shoppingList" :key="item.id" :shoppingList="item" />
    </ul>
  </div>
</template>
