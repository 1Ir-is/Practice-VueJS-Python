<script setup>
import { ref } from 'vue'

const isLoggedIn = ref(true)
const isVisible = ref(true)
const userStatus = ref('online')

const toggleLogin = () => {
  isLoggedIn.value = !isLoggedIn.value
}

const toggleShow = () => {
  isVisible.value = !isVisible.value
}

const changeStatus = () => {
  if (userStatus.value === 'online') {
    userStatus.value = 'away'
  } else if (userStatus.value === 'away') {
    userStatus.value = 'busy'
  } else if (userStatus.value === 'busy') {
    userStatus.value = 'online'
  }
}
</script>

<template>
  <div>
    <h1 v-if="isLoggedIn">Chao mung nguoi dung da dang nhap</h1>
    <h1 v-else>Chao mung khach</h1>
    <button @click="toggleLogin">{{ isLoggedIn ? 'Dang xuat' : 'Dang nhap' }}</button>
    <br />
    <h1 v-if="userStatus === 'online'">Nguoi dung dang online</h1>
    <h1 v-else-if="userStatus === 'away'">Nguoi dung dang vang mat</h1>
    <h1 v-else-if="userStatus === 'busy'">Nguoi dung dang ban</h1>
    <h1 v-else>Khong ro trang thai</h1>
    <button @click="changeStatus">Thay doi trang thai</button>

    <br />

    <h1 v-show="isVisible">Noi dung nay an hoac hien thi</h1>
    <button @click="toggleShow">{{ isVisible ? 'An' : 'Hien' }}</button>
  </div>
</template>
