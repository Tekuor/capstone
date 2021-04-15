<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import { getInstance } from "@/auth";
import jwt_decode from "jwt-decode";

export default {
  async mounted(){
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
                let decoded = jwt_decode(authToken);
                let user = Object.assign({}, this.$auth.user, {permissions: decoded.permissions})
                localStorage.setItem('user', JSON.stringify(user))
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
    color: #2c3e50;
  }
</style>
