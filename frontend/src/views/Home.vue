<template>
  <div class="home">
    <div id="main">
      <div class="is-size-1 has-text-weight-bold is-capitalized" style="color:#990033">Casting actors just got simpler!</div>
      <div class="pt-4"><b-button type="is-primary" @click="login" style="background-color:#990033" size="is-medium">Get Started</b-button></div>
    </div>
    <!-- <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" /> -->

    <!-- Check that the SDK client is not currently loading before accessing is methods -->
    <!-- <div v-if="!$auth.loading"> -->
      <!-- show login when not authenticated -->
      <!-- <button v-if="!$auth.isAuthenticated" @click="login">Log in</button> -->
      <!-- show logout when authenticated -->
      <!-- <button v-if="$auth.isAuthenticated" @click="logout">Log out</button>
    </div> -->
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  },
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    }
  }
}
</script>

<style scoped>
  .home {
    height:100%;
    background: 
    linear-gradient(
      rgba(232, 232, 232, 0.45), 
      rgba(232, 232, 232, 0.45)
    ),
    url("../assets/background.jpg");
  }
  #main{
    padding-top:18%
  }
</style>