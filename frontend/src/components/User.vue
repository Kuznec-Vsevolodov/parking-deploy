<template>
  <div>
    <b-container>
      <h2 align="center">{{name}}</h2>
      <div class="balance-info">
        <p>Ваш баланс составляет: <span>{{this.wallet}}</span></p>

        <form>
            <label>Введите сумму, на которую хотите пополнить ваш баланс</label>
          <div class="input-group">
            <input type="number" v-model="income" class="income-input" name="income-input">
            <button @click="incomeWallet" class="btn btn-primary income-button">Пополнить</button>
          </div>
        </form>
        <p v-if="success" class="bg-success">Поздравляем</p>
      </div>

      <div class="booked_places">
        <p>Ваши забронированные места: </p>
        <div v-for="user_place in user_places" :key="user_place.id">
          <p>Колонна: {{user_place.column}}</p>
          <p>Ряд: {{user_place.row}}</p>
          <p><router-link :to="{path: `/sectors/`+user_place.sector_id}" class="card-link">Просмотреть ещё места в секторе</router-link></p>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
      name: '',
      id: 0,
      wallet: 0,
      user_places: [],
      income: 0,
      success: false
    }
  },
  created(){
    try {
        var walletId = this.$route.params.id-1
        axios.get('http://127.0.0.1:8000/demo/wallets/'+walletId,
            { headers: { Authorization: `Bearer ${localStorage.accessToken}` }})
            .then((response) => {
                  this.wallet = response.data.wallet
        })
        console.log(this.wallet)
    } catch (error) {
      console.error('Ошибка подключения');
    }
    axios.get('http://127.0.0.1:8000/demo/get-users-places/'+this.$route.params.id,
            { headers: { Authorization: `Bearer ${localStorage.accessToken}` }})
            .then((response) => {
                  console.log(response.data)
                  this.user_places = response.data
        })
  },
  mounted() {
    if(localStorage.name) {
      this.name = localStorage.name
      this.id = localStorage.userId
    }
  },
  methods:{
    incomeWallet: function (){
      var walletId = this.$route.params.id-1;
      var price = Number.parseInt(this.income)
      if(price < 0){
        price = -price
      }
      axios.put('http://127.0.0.1:8000/demo/wallets/'+walletId+'/', {
              "income": price
            },
            { headers: { Authorization: `Bearer ${localStorage.accessToken}` }})
            .then((response) => {
                  console.log(response.data)
                  console.log("отлично, вы пополнили баланс")
                  this.wallet = response.data.wallet
                  this.success = true
                  this.income = 0
            })
            .catch((err) => {
                  console.log(err)
                  this.success = false
            })
    }
  }
}
</script>

<style scoped>
.input-group{
  display: flex;
  align-items: flex-end;

}
.income-input{
  border-radius: 50px;
  width: 150px;
  border: 1px solid #3c763d;
  height: 30px;
  padding-left: 10px;
}
.income-button{
  height: 30px;
  border-radius: 50px !important;
  margin-left: 15px;
  line-height: 15px;
  font-size: 15px;
}
</style>