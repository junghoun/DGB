<template>
  
  <v-app v-if="$route.path == '/home'">
    <v-main><router-view></router-view>
    <nav-bar></nav-bar>
    </v-main>
  </v-app>
  <v-app v-else-if="$route.path =='/'">
    <v-main>
      <router-view></router-view>
    <nav-bar></nav-bar>
    </v-main>
  </v-app>
  <v-app v-else-if="$route.path == '/login'">
    <v-main> <router-view></router-view> </v-main>
    <nav-bar></nav-bar>
  </v-app>
  <v-app v-else-if="$route.path == '/signup'">
    <v-main>
      <router-view></router-view>
      <nav-bar></nav-bar>
    </v-main>
  </v-app>
  
  <v-app v-else>
    <v-main>
      <router-view></router-view>
      <side-bar></side-bar>
    </v-main>
  </v-app>
  
</template>


<script>


import SideBar from './components/common/SideBar.vue';
import NavBar from './components/common/NavBar.vue';


export default {
  name: "App",
  components: { SideBar, NavBar},

  data() {
    return {};
  },
};
</script>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
</style>