<template>
<div class="navbar-holder">
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand>
      <router-link :to="{path: `/`}">
            CarBook
      </router-link>
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item>
          <router-link :to="{path: `/events`}">
            Events
          </router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link :to="{path: `/places`}">
            Places
          </router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link :to="{path: `events/`}">
            Booking
          </router-link>
        </b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em v-if="name == ''">User</em>
            <em v-else>{{name}}</em>
          </template>
          <b-dropdown-item v-if="name == ''"><router-link :to="{path: `/login`}" class="log_link">Sign in</router-link></b-dropdown-item>
          <div v-else>
            <b-dropdown-item><router-link :to="{path: `/profile/`+id}" class="log_link">Profile</router-link></b-dropdown-item>
            <b-dropdown-item @click="LogOut">Log out</b-dropdown-item>
          </div>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>

  <div class="b-container"></div>

</div>
</template>

<script>
export default {
  data(){
    return{
      name: "",
      id: 0
    }
  },
  mounted() {
    console.log(localStorage.name)
    if (localStorage.name && localStorage.userId) {
      this.name = localStorage.name
      this.id = localStorage.userId
    }
  },
  methods:{
    LogOut: function (){
      localStorage.name = '';
      localStorage.accessToken = null;
      localStorage.refreshToken = null;
      document.location.href = 'http://localhost:8080/';
    }
  }
}
</script>

<style scoped>
  .navbar-holder{
    margin-bottom: 20px;
  }
  a{
    color: #fff;
  }
  a:hover{
    color: #fff;
    text-decoration: none;
  }
  .log_link{
    color: #000
  }
</style>