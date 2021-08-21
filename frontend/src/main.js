import Vue from 'vue'
import App from './App.vue'
import router from "./router"
import store from "./store"
import vuetify from './plugins/vuetify'
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";
import VueFullPage from 'vue-fullpage.js'

Vue.use(VueMaterial);
Vue.use(VueFullPage);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
  vuetify,
  components: { App }
}).$mount("#app");
