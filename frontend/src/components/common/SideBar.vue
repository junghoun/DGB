<template>
  <nav style="font-family:'Jua';">
    <v-navigation-drawer
      permanent
      expand-on-hover
      app
      class="darkgrey accent-2"
    >
      <v-list>
        <v-list-item class="d-flex justify-center">
          <v-list-item-avatar>
            <v-img src="profile.gif"></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item >
          <v-list-item-icon>
            <span class="material-icons">
              face
            </span>
          </v-list-item-icon>
          <v-list-item-content
            class="title d-flex justify-center"
            style="font-family:'Jua';"
          >
            <v-list-item-title style="font-family:'Jua';">
              {{user.userName}}
            </v-list-item-title>
            <v-list-item-subtitle style="font-family:'Jua';"
              > {{user.phoneNumber | phone}} </v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>


        <v-list-item>
          <v-list-item-icon>
            <span class="material-icons">
              attach_money
            </span>
          </v-list-item-icon>
          <v-list-item-content
            class="title d-flex justify-center"
            style="font-family:'Jua';"
          >
            <v-list-item-title style="font-family:'Jua';">
              현금
            </v-list-item-title>
            <v-list-item-subtitle style="font-family:'Jua';"
              > {{user.cash | comma}} 원</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list nav dense>
        <v-list-item to="/homePage">
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
          <v-list-item-title>HOME</v-list-item-title>
        </v-list-item>
        <v-list-item to="/remit" v-if = "count != 0">
          <v-list-item-icon>
            <v-icon>arrow_right_alt</v-icon>
          </v-list-item-icon>
          <v-list-item-title>송금</v-list-item-title>
        </v-list-item>
        <v-list-item to="/trans" v-if = "count != 0">
          <v-list-item-icon>
            <v-icon>view_list</v-icon>
          </v-list-item-icon>
          <v-list-item-title>거래내역</v-list-item-title>
        </v-list-item>
        <v-list-item to="/adver">
          <v-list-item-icon>
            <v-icon>mdi-star</v-icon>
          </v-list-item-icon>
          <v-list-item-title>상품몰</v-list-item-title>
        </v-list-item>
        <v-list-item to="/account">
          <v-list-item-icon>
            <v-icon>view_in_ar</v-icon>
          </v-list-item-icon>
          <v-list-item-title>계좌개설</v-list-item-title>
        </v-list-item>

        <v-list-item
          @click="onLogout"
          style="position:fixed; bottom:0px; width:100%;"
        >
          <v-list-item-icon>
            <v-icon>exit_to_app</v-icon>
          </v-list-item-icon>
          <v-list-item-title>로그아웃</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>

  

</template>

<script>
import { mapActions, mapState } from "vuex";
import Filters from "@/utils/filters.js";

export default {
  filters : Filters,
  data() {
    return {
      
      drawer: true,
      count : 0,
    };
  },
  computed: {
    ...mapState({
      user: "user",
    }),
  },
  created() {
    this.getUserinfo();
    this.getCount();
  },
  methods: {
    ...mapActions([
      "USERINFO",
      "GET_FETCHCOUNT",
      ]),
    async onLogout() {
      await this.$store.dispatch("LOGOUT");
      this.$router.push("/login");
    },
    getUserinfo() {
      this.USERINFO().then(() => {
        
      });
    },
    async getCount() {
      await this.GET_FETCHCOUNT().then((response) => {
        this.count = response.data.count;
      })
    },
  },
};
</script>
