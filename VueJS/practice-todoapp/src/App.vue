<script setup>
import { reactive, ref } from 'vue'

const newToDo = ref('')

const todos = reactive([
  {
    id: 1,
    text: 'Learn VueJS',
    isEditing: false,
  },
  {
    id: 2,
    text: 'Build TodoApp',
    isEditing: false,
  },
])

const addToDo = () => {
  if (newToDo.value.trim() === '') {
    return
  } else {
    const todo = {
      id: todos.length + 1,
      text: newToDo.value,
    }
    todos.push(todo)
    newToDo.value = ''
  }
}

const deleteToDo = (id) => {
  const index = todos.findIndex((todo) => todo.id === id)
  if (index !== -1) {
    todos.splice(index, 1)
  }
}

const startEdit = (todo) => {
  todo.isEditing = true
  todo.editText = todo.text
}

const saveEdit = (todo) => {
  const text = todo.editText.trim()
  if (text === '') return
  todo.text = text
  todo.isEditing = false
}

const cancelEdit = (todo) => {
  todo.isEditing = false
}
</script>

<template>
  <div>
    <h1>Todo App</h1>

    <div>
      <input type="text" v-model="newToDo" placeholder="Input" @keyup.enter="addToDo" />
      <button @click="addToDo">Add</button>
    </div>

    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <template v-if="todo.isEditing">
          <input
            type="text"
            v-model="todo.editText"
            placeholder="Edit"
            @keyup.enter="saveEdit(todo)"
          />
          <!-- <button @click="saveEdit(todo)">Save</button> -->
          <button v-on:click="saveEdit(todo)">Save</button>
          <button @click="cancelEdit(todo)">Cancel</button>
        </template>

        <template v-else>
          {{ todo.text }}
          <button @click="startEdit(todo)">Edit</button>
          <button @click="deleteToDo(todo.id)">Delete</button>
        </template>
      </li>
    </ul>
  </div>
</template>
