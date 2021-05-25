<template>
  <div class="hello">
    <div>
      <h1>Добро пожаловать на CarBook</h1>
      <h2>Скорее подберите мероприятие и забронируйте место</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello div{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 800px;
}
</style>
