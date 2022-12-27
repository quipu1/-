<template>
  <v-app id="app">
    <Header v-if="!$route.meta.hideHeader"/>
    <SideBar v-if="!$route.meta.hideSideBar"/>
    <router-view/>
  </v-app>
  
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import Header from '@/components/Header.vue'

export default ({
  components: {
    Header,
    SideBar,
  },
})
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');
* {
  font-family: 'Noto Sans KR', sans-serif; 
}
// #app {
//   font-family: Avenir, Helvetica, Arial, sans-serif;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
//   text-align: center;
//   color: #2c3e50;
// }

// #nav {
//   padding: 30px;

//   a {
//     font-weight: bold;
//     color: #2c3e50;

//     &.router-link-exact-active {
//       color: #42b983;
//     }
//   }
// }
</style>
