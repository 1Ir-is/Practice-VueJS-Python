<script setup>
import { computed, reactive, ref } from 'vue'

const firstName = ref('Huynh Minh')
const lastName = ref('Huy')

const fullName = computed({
  get() {
    return firstName.value + ' ' + lastName.value
  },
  set(newValue) {
    ;[firstName.value, lastName.value] = newValue.split(',')
  },
})

const changeFullName = () => {
  fullName.value = 'Nguyen Duc,Vinh'
}
</script>

<template>
  <div>
    <p>First Name: {{ firstName }}</p>
    <p>Last Name: {{ lastName }}</p>
    <p>FullName: {{ fullName }}</p>
    <button @click="changeFullName">Change fullname</button>
  </div>
</template>
