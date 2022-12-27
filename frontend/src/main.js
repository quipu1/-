import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import store from './store'
import router from './router'
import VueGeolocationApi from 'vue-geolocation-api'

Vue.config.productionTip = false
Vue.use(VueGeolocationApi/*, { ...options } */)

new Vue({
  vuetify,
  store,
  router,
  render: h => h(App)
}).$mount('#app')
