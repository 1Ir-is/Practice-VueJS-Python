<script setup>
const props = defineProps({
  shoppingList: Object,
})
</script>

<template>
  <li>{{ shoppingList.name }} - {{ shoppingList.quantity }}</li>
</template>
