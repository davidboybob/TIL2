<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="alert alert-danger" role="alert">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>
      </div>
      <div class="form-group">
        <label for="id">ID : </label>
        <input 
          type="text" 
          class="form-control" 
          id="id" 
          placeholder="아이디를 입력해 주셍요"
          v-model="credentials.username"
          
        >  
      </div>
      <div class="form-group">
        <label for="id">PASSWORD</label>
        <input 
          type="password" 
          class="form-control" 
          id="password" 
          placeholder="비밀번호 입력 주서용"
          v-model="credentials.password"  
          
        >
      </div>
      <button type="submit" class="btn btn-primary" @click="login">로그인</button>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'
  import router from '../router'
  export default {
    name: 'LoginForm',
    data() {
      return {
        credentials: {
          username:'',
          password: '',
        },
        loading: false,
        errors: [],
        
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          // 1. django jwt 를 생성하는 주소로 요청을 보냄
          // 이때 post 요청으로 보내야 하며 사용자가 입력한 로그인 정보(credentials)를 같이 넘겨야 함.
          this.loading = true
          axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
            .then(res => {
              this.$session.start()
              this.$session.set('jwt', res.data.token)
              //router 사용 전 import 해줘야함. 
              router.push('/')

              // 2. 로그인 이후에는 loading 의 상태를 다시 false로 변경
              // 그래야 spinner가 계속 돌지 않고 로그인 form 을 받아 볼 수 있음.
              // this.loading = false
              
            })
            .catch(err => {
              // 3. 로그인 실패 시 loading 의 상태를 다시 false로 변경
              this.loading = false
              console.log(err)
            })
        } else {
          console.log('로그인 검증 실패')
        }
      },
      checkForm() {
        this.errors = []
        if (!this.credentials.username) {
          this.errors.push("아이디를 입력해주세요.")
        }
        if (this.credentials.password.length < 8) {
          this.errors.push("비밀번호는 8자 이상 입력해주세요.")
        }
        if (this.errors.length === 0) {
          return true
        }
      }
    },
  }
</script>
  

<style scoped>

</style>