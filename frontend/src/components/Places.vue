<template>
  <div>
    <h2 align="center" style="margin-bottom: 20px">Места проведения мероприятий</h2>
    <b-container>
      <b-row>
      <div
        v-for="place in places"
        :key="place.id">
      <b-card
        :title="place.title"
        tag="article"
        style="width: 300px;"
        class="mb-2 ml-2 mr-2"
      >
        <b-card-text>
          Адрес: <span>{{place.address}}</span>
          <br>
        </b-card-text>

        <b-button><router-link :to="{path: `/places/`+place.id}" class="card-link">Просмотреть позицию</router-link></b-button>
      </b-card>
    </div>
    </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
      places: []
    }
  },
  async created() {
    var response = await axios.get('http://127.0.0.1:8000/demo/places/').then((response) => {
                  console.log(response.data)
                  return response.data
        })
        this.places = await response
    // try {
    //     var response = await axios.get('http://127.0.0.1:8000/demo/red-places/', { headers: { Authorization: `Bearer ${'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxMjg3MjI1LCJqdGkiOiJjYzUxYjk1ODlkYTU0OGMxOTY2YWQwZGFjMTEwMmUwNyIsInVzZXJfaWQiOjR9.eVY0qwqk7hb1JHcQR7x7er6ynq0LzKkqy_lBTcwVI38'}` }}).then((response) => {
    //               console.log(response.data)
    //               return response.data
    //     })
    //     this.places = await response
    // } catch (error) {
    //   console.error('Вы не авторизированы');
    // }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card-link{
    color: #fff;
  }
</style>