<template>
  <div class="todo-list">
    <h2>{{ category }}</h2>
    <input type="text" v-model="newTodo" @keyup.enter="addTodo">
    <button @click="addTodo">+</button>
    <li v-for="todo in todos" :class="{ completed: todo.completed }" :key="todo.id">
      <span>{{ todo.content }}</span>
      <button @click="removeTodo(todo.id)">X</button>
    </li>
  </div>
</template>

<script>
  //내보내기
  export default {
    props: {
      category: {
        type: String, //문자열 
        required: true, // 반드시 필요한 값
        validator: function (value) {
          if (value.length < 5) {
            return true
          } else {
            return false
          }
        }
      }
    },

    data: function () {
      return {
        todos: [],
        newTodo: '',
      }
    },

    methods: {
      addTodo: function () {
        if (this.newTodo.length != 0) {
          this.todos.push({
            id: Date.now(),
            content: this.newTodo,
            completed: false,
          })
        }
        this.newTodo = ''
      },
      removeTodo: function (todoId) {
        this.todos = this.todos.filter(todo => {
          return todo.id !== todoId
        })
      },
    },
  }
</script>

<style>
  .todo-list {
    display: inline-block;
    width: 33%;
  }
</style>