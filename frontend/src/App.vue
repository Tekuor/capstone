<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import { getInstance } from "@/auth";

export default {
  async created(){
    await this.retrieveTokenFromAuth()
  },
  methods: {
    retrieveTokenFromAuth() {
      return new Promise((resolve, reject) => {
        const instance = getInstance();
        instance.$watch("loading", loading => {
          if (loading === false && instance.isAuthenticated) {
            instance
              .getTokenSilently()
              .then(authToken => {
                localStorage.setItem('token', authToken)
                localStorage.setItem('user', JSON.stringify(this.$auth.user))
                resolve(authToken);
              })
              .catch(error => {
                reject(error);
              });
          }
        });
      });
    }
  }
}
</script>

<style>
  #app {
    height:100%;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
</style>
