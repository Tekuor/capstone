import Vue from "vue";
import App from "./App.vue";
import router from './router'
import Buefy from 'buefy'
// import 'buefy/dist/buefy.css'
import './buefy.scss'

// Import the Auth0 configuration
import { domain, clientId } from "../auth_config.json";

// Import the plugin here
import { Auth0Plugin } from "./auth";

Vue.use(Buefy)
// Install the authentication plugin here
Vue.use(Auth0Plugin, {
  domain,
  clientId,
  audience: 'agency',
  response_type: 'token',
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");