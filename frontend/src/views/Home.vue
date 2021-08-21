<template>
  <div>
    <full-page>
      <div class="section">
        <v-app>
            <v-app>
                <home-first></home-first>
            </v-app>
        </v-app>
      </div>
      <div class="section">
        <v-app>
            <v-app>
                <home-second></home-second>
            </v-app>
        </v-app>
      </div>
      <div class="section">
        <v-app>
            <v-app>
                <home-third></home-third>
            </v-app>
        </v-app>
      </div>
      <div class="section">
        <v-app>
            <v-app>
                <home-fourth></home-fourth>
            </v-app>
        </v-app>
      </div>
      <div class="section">
        <v-app>
            <v-app>
                <home-fifth></home-fifth>
            </v-app>
        </v-app>
      </div>
      <div class="section">
        <v-app>
            <v-app>
                <home-sixth></home-sixth>
            </v-app>
        </v-app>
      </div>
    </full-page>
  </div>
</template>

<script>

import HomeFirst from '@/components/home/HomeFirst.vue';
import HomeSecond from '@/components/home/HomeSecond.vue';
import HomeThird from '@/components/home/HomeThird.vue';
import HomeFourth from '@/components/home/HomeFourth.vue';
import HomeFifth from '@/components/home/HomeFifth.vue';
import HomeSixth from '@/components/home/HomeSixth.vue';

export default {
    name : 'Home',
    components : {
        HomeFirst,
        HomeSecond,
        HomeThird,
        HomeFourth,
        HomeFifth,
        HomeSixth,
    }
    
}
</script>

<style>

</style>