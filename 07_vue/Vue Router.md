# Vue Router

## 개요

:kissing_smiling_eyes: 맨땅의 헤딩 유튜브를 보고, 정리한 내용.

## 1. BASIC - 1

주소 : `www.yourwebsite.com/user`

`/`이후의 주소값들을 Vue Router 가 인지함

![Vue Router _ VueJS 3 _ Learning the Basics -1 - YouTube - Chrome 2020-01-30 오후 11_40_20 (2)](https://user-images.githubusercontent.com/52685322/73460122-47287300-43bb-11ea-99d1-5c8b56b6b374.png)

컴포넌트들의 요소들이 합쳐져서 Router를 통해서 화면으로 송출되는 역할을 담당함.



```vue

```



### 1.1 router.js

```javascript

// ex)
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter) // 뷰라우터 선언

const routes = [
  { // 객체 안에서 연결 지어줘서
    path: '/',  // 경로 (url)
    name: 'home', // 주소창에 쓰여질 뒷부분의 부분(별칭)
    component: Home // 컴포넌트
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```



```vue
// App.vue

<template>
  <router-view></router-view>  
</template>


```

