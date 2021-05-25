<template>
  <div>
    <b-container>
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

        <b-button :href="'http://127.0.0.1:8000/demo/sectors/'+sector.id" variant="primary">Go somewhere</b-button>
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
      sectors: []
    }
  },
  async created() {
    var response = await fetch('http://127.0.0.1:8000/demo/sectors/')
    this.sectors = await response.json()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>