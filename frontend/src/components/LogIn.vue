<template>
  <div>
    <div>Вы уже авторизированы</div>
     <h1>Sign in</h1>
     <label>Name</label>
     <input required v-model="username" type="text" placeholder="Name"/>
     <label>Password</label>
     <input required v-model="password" type="password" placeholder="Password"/>
     <hr/>
     <button v-on:click="Login">Login</button>
  </div>

</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
      username: '',
      password: ''
    }
  },
  methods: {
      Login: function () {
        axios.post('http://127.0.0.1:8000/demo/token/', {
          "username": this.username,
          "password": this.password
        })
        .then((response) => {
          console.log(response.data);
          localStorage.accessToken = response.data.access;
          localStorage.refreshToken = response.data.refresh;
          localStorage.name = this.username;
          console.log(localStorage.accessToken)
          setTimeout(() => {  location.href = 'http://localhost:8080/'; }, 1000);

        })
        .catch((error) => {
          console.log(error);
        });
      }

  },
  mounted(){
    if(!localStorage.accessToken){
      localStorage.accessToken = null
    }

    console.log(localStorage.accessToken)
  }
}

</script>

<style scoped>

</style>