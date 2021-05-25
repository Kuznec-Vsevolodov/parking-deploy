<template>
  <div>
    <h3 align="center">Изменить данные позиции</h3>
    <b-container class="input-info-group">
        <input type="text" v-model="title" :placeholder="sector_data.title">
        <input type="number" v-model="size" :placeholder="sector_data.size">
        <input type="number" v-model="rows" :placeholder="sector_data.rows">
        <input type="number" v-model="columns" :placeholder="sector_data.columns">
        <input type="number" v-model="price" :placeholder="sector_data.price">
        <input type="text" v-model="description" :placeholder="sector_data.description">
        <button @click="sendData">Отправить данные</button>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
      sector_data: [],
      title: '',
      size: 0,
      rows: 0,
      columns: 0,
      price: 0,
      description: ''
    }
  },
  created() {
    axios.get('http://127.0.0.1:8000/demo/sectors/'+this.$route.params.id,
        { headers: { Authorization: `Bearer ${localStorage.accessToken}` }})
        .then((response) => {
          this.sector_data = response.data
          this.title = response.data.title
          this.size = response.data.size
          this.rows = response.data.rows
          this.columns = response.data.columns
          this.price = response.data.price
          this.description = response.data.description
    });
  },
  methods: {
      fileUpload(){
        this.file = this.$refs.image.files[0];
      },
      sendData(){
        axios.put('http://127.0.0.1:8000/demo/sectors/'+this.$route.params.id+'/',
            { 'title': this.title, 'size': this.size, 'rows': this.rows, 'columns': this.columns, 'price': this.price, 'description': this.description},
            { headers: { Authorization: `Bearer ${localStorage.accessToken}` }})
        .then((response) => {
          this.sector_data = response.data
          this.title = response.data.title
          this.size = response.data.size
          this.rows = response.data.rows
          this.columns = response.data.columns
          this.price = response.data.price
          this.description = response.data.description
        });
      }
  }
}
</script>

<style scoped>
.input-info-group{
  display: flex;
  flex-direction: column;
  margin-top: 50px;
}
.input-info-group input{
  border: 2px solid #CCCCCC;
  border-radius: 50px;
  height: 35px;
  margin-bottom: 15px;
  padding-left: 10px;
}
.input-info-group button{
  border: 2px solid #000;
  background: #fff;
  border-radius: 50px;
  height: 35px;
  color: #000000;
  font-weight: bold;
}
</style>