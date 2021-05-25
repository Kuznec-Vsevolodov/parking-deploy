<template>
  <div class="main-container">
      <div class="place col-md-3">
        <img :src="'http://127.0.0.1:8000'+place.general_scheme" alt="" style="width: 400px;">
        <div class="sector-top">
          <p>{{place.title}}</p>
        </div>
        <div class="info">
          <p>Адрес: <span>{{place.address}}</span></p>
        </div>
      </div>
      <div v-if="user == place.owner">
        <router-link :to="{path: `/places/red-places/`+place.id}">Редактировать информацию</router-link>
      </div>
      <b-container>
        <p class="sec-group-gen-info">Располагающиеся здесь сектора:</p>
      <b-row>
      <div
        v-for="sector in sectors"
        :key="sector.id">
      <b-card
        :title="sector.title"
        tag="article"
        style="width: 300px;"
        class="mb-2 ml-2 mr-2"
      >
        <b-card-text>
          Объём мест: <span>{{sector.size}}</span>
          <br>
          Цена за место в данном секторе: <span>{{sector.price}}</span>
        </b-card-text>
        <div v-if="user == place.owner">
          <router-link :to="{path: `/sectors/red-sectors/`+sector.id}">Редактировать информацию</router-link>
        </div>
        <b-button><router-link :to="{path: `/sectors/`+sector.id}" class="card-link">Просмотреть позицию</router-link></b-button>
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
      place: [],
      sectors: [],
      user: 0,
    }
  },
  async created() {
    this.user = localStorage.userId;
    var response_place = await fetch('http://127.0.0.1:8000/demo/places/'+this.$route.params.id);
    var response_sector = await fetch('http://127.0.0.1:8000/demo/places/sectors/'+this.$route.params.id)
    this.place = await response_place.json()
    this.sectors = await response_sector.json()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card-link{
    color: #fff;
  }
  .main-container{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .place{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 30px;
  }
  .sector-top{
    margin-top: 20px;
  }
  .sector-top p{
    font-size: 20px;
    font-weight: bold;
  }
  .sec-group-gen-info{
    font-weight: bold;
  }
</style>