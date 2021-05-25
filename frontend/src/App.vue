<template>
  <div id="app">
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>

<script>

import Navbar from "@/components/Navbar";
import axios from "axios";

export default {
  name: 'App',
  data(){
    return{
    }
  },
  components:{
    Navbar
  },
  async created() {
    if(localStorage.accessToken && localStorage.accessToken != null){
      try {
        var response = await axios.get('http://127.0.0.1:8000/demo/get-data/', { headers: { Authorization: `Bearer ${localStorage.accessToken}` }}).then((response) => {
                    return response
          })
        localStorage.name = response.data.name
        localStorage.userId = response.data.user
      } catch (error) {
            axios.post('http://127.0.0.1:8000/demo/token/refresh/', {
              "refresh": localStorage.refreshToken
            })
            .then((response) => {
              console.log(response.data);
              console.log(response.data.access);
              localStorage.accessToken = response.data.access;
              console.log(localStorage.accessToken)
              axios.get('http://127.0.0.1:8000/demo/get-data/', { headers: { Authorization: `Bearer ${localStorage.accessToken}` }}).then((response) => {
                    localStorage.name = response.data.name
                    localStorage.userId = response.data.id
              })
            })
      }
    }
  }
}
</script>

<style>
</style>
