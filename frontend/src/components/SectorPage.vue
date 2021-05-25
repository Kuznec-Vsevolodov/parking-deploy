<template>
  <div>
      <b-container>
          <div class="place col-md-3">
          <div class="sector-top">
            <p>{{sector.title}}</p>
          </div>
          <div class="info">
            <p>Цена: <span>{{sector.price}}</span></p>
          </div>
        </div>

<!--      <div class="columns" v-for="n in columns" :key="n">-->
<!--        {{n}}-->
<!--      </div>-->
          <div class="place-row">
            <div v-for="n in columns" :key="n">
              <div v-for="place in places" :key="place.id">
                <div v-if="place.column == n">
                  <input type="checkbox" :value="['ряд: '+ place.row + ', коллонна: ' + place.column + '; ', place.id]" v-model="selectedPlaces">
                </div>
              </div>
            </div>
          </div>
          <p>Забронированные места: <span v-for="place in selectedPlaces" :key="place[1]">{{place[0]}}</span></p>

          <p>Выберите мероприятие для бронирования</p>
          <select v-model="selectedEvent">
            <option v-for="event in events" :key="event.id" :value="event.id">{{event.title}}</option>
          </select>
          <b-button variant="primary" @click="bookPlace">Забронировать</b-button>
      </b-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
      places: [],
      sector: [],
      columns: 0,
      rows: 0,
      n: 1,
      selectedPlaces: [],
      events: [],
      selectedEvent: 0
    }
  },
  async created() {
    console.log(this.$route.params.id)
    var response_events = await fetch('http://127.0.0.1:8000/demo/events/')
    this.events = await response_events.json()
    var response_place = await fetch('http://127.0.0.1:8000/demo/sectors/parking_places/'+this.$route.params.id);
    var response_sector = await fetch('http://127.0.0.1:8000/demo/sectors/'+this.$route.params.id)
    this.places = await response_place.json()
    this.sector = await response_sector.json()
    this.columns = this.sector.columns;
    this.rows = this.sector.rows;
    console.log(this.columns)
    console.log(this.rows)
  },
  methods:{
    bookPlace: function (){
        if(this.selectedEvent == 0 || this.selectedPlaces.length == 0){
          console.log("Некорректно заданы значения")
        }else{
         for(var i = 0; i < this.selectedPlaces.length; i++){
          axios.post('http://127.0.0.1:8000/demo/booked_places/',
          { "parking_place": this.selectedPlaces[i][1], "event_id": this.selectedEvent},
          { headers: { Authorization: `Bearer ${localStorage.accessToken}` }})
          .then((response) => {
                      console.log("Поздравляем с бронью")
                      console.log(response.data)
          })
        }
        }
    }
  }
}
</script>

<style scoped>
  .place-row{
    display: flex;
    width: 100%;
    justify-content: center;
  }
</style>