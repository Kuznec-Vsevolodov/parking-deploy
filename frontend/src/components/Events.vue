<template>
  <div>
     <h2 align="center" style="margin-bottom: 20px">Места проведения мероприятий</h2>
    <b-container>
      <b-row>
      <div
        v-for="event in events"
        :key="event.id">
      <b-card
        :title="event.title"
        tag="article"
        style="width: 300px;"
        class="mb-2 ml-2 mr-2"
      >
        <img :src="'http://127.0.0.1:8000'+event.event_cover" alt="" width="100%">
        <b-card-text>
          Описание: <span>{{event.description}}</span>
          <br>
        </b-card-text>

        <b-button><router-link :to="{path: `/places/`+event.place}" class="card-link">Просмотреть место проведения</router-link></b-button>
      </b-card>
    </div>
    </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  data(){
    return{
      events: []
    }
  },
  async created() {
    var response = await fetch('http://127.0.0.1:8000/demo/events/')
    this.events = await response.json()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card-link{
    color: #fff;
    font-size: 15px;
  }
</style>