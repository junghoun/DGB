<template>
  <v-app :style="{ background: $vuetify.theme.themes.light.background }" style="font-family:'Jua';">
       
    <v-container class="cont">
      <v-layout>

        <v-app style="background-color: grey lighten-1;" class="rounded mx-auto">

          <!-- <v-row style="font-family:'Jua';"> -->
            
              <v-container >
                <v-flex>
                    <v-row style = "margin-top : 50px; ">
                      <v-col cols="12" md="12" style = "min-width : 450px">
                        <v-card elevation="10" style="border-radius: 40px !important; height : auto; width : 1000px;">
                          <v-list>
                            <v-list-item>
                              <v-list-item-title class="headline font-weight-bold" style="text-align : center;">
                                계좌 개설
                              </v-list-item-title>
                              
                            </v-list-item>
                            
                            <v-divider class="mx-4" style = "display : flex;"></v-divider>
                            <v-row  v-for="item in test" :key="item"> 
                              <v-col cols="12" md="1">
                                
                              </v-col>
                              <v-col cols="12" md="2" style="text-align : center; margin-top : 25px; ">
                                <v-icon>shop</v-icon>
                              </v-col>
                              <v-col cols="12" md="2">
                                <v-img :src="item.img" width = "100px"></v-img>
                              </v-col>
                              <v-col cols="12" md="4" style="text-align : center; margin-top : 25px;">
                                <h2>
                                  {{item.title}}
                                </h2>
                              </v-col>
                              <v-col cols="12" md="2">
                                <v-btn style="text-align : center; margin-top : 25px; " color="blue white--text">
                                    <v-icon left small>done_outline</v-icon>
                                      <spen @click="show(item.title, item.img)">개설</spen>
                                </v-btn>
                              </v-col>
                            </v-row>


                          </v-list>
                        </v-card>
                        
                      </v-col>
                    </v-row>
                    <v-row style = "margin-top : 50px;">
                      <v-col cols="12" md="4">
                                
                      </v-col>
                      
                      <v-col cols="12" md="4">
                        <v-card v-if = this.title style = "height : 400px; text-align : center;" >
                          <h2>
                            {{this.title}}
                          </h2>
                          <v-img :src="this.card"></v-img>
                          <h2 style = "margin-top : 20px;">
                          비밀번호
                          </h2>
                          <v-text-field
                              prepend-icon="lock"
                              placeholder="비밀번호 4자리."
                              type="Password"
                              style=""
                              maxlength='4'
                              v-model="pw"
                            ></v-text-field>

                            <button color="blue white--text" @click="goAcc">
                              <v-icon>power_settings_new</v-icon>개설
                            </button>
                        </v-card>
                      </v-col>
                    </v-row>
                </v-flex>
              </v-container>
            
            

              <v-dialog
                  v-model="flag"
                  persistent
                  max-width="350px"
                  height="300px;"
                  
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>비밀번호 입력하세요!</div>
                    </v-card-title>
                  </v-card>
                </v-dialog>


                <v-dialog
                  v-model="finish"
                  persistent
                  max-width="350px"
                  height="300px;"
                  
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>개설 완료!!!!</div>
                    </v-card-title>
                  </v-card>
                </v-dialog>

          <!-- </v-row> -->
        </v-app>
      </v-layout>

    </v-container>

  </v-app>
</template>
<script>

import { mapActions, mapState } from "vuex";



export default {
  
  data() {
    return {
      
      test: [
        { img: "card1.png", title: "  Dandi  체크카드" },
        { img: "card2.png", title: "영플러스 체크카드" },
        { img: "card4.png", title: "  Green  체크카드" },
        { img: "card5.png", title: "아이행복 체크카드" },
      ],

      title : "",
      card : "",
      pw : "",
      flag : false,
      finish : false,
      
    };
  },
  computed: {
    ...mapState({
      user: "user",
    }),
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
  },
  created() {
    this.getUserinfo();
    
  },
  
  methods: {
    ...mapActions([
      "USERINFO",
      "INSERT_ACCOUNT",
      
      ]),
    
    getUserinfo() {
      this.USERINFO().then(() => {
        console.log(this.user);
        
      });
    },
    
    show(value, card){
      
      this.title = value;
      this.card =  card;
    }
    ,
    goAcc(){
      if(this.pw.length != 4) {
        
        this.flag = true;
        setTimeout(() => {
        this.flag = false;
      }, 1000);
      }else{
        
        this.addAcc(1, this.pw);
        
        this.$router.go();
      }
    },
    async addAcc(type, password) {
      var AccData = {
        type : type,
        password : password
      }
      console.log(AccData)
      await this.INSERT_ACCOUNT(AccData).then(() => {
      })
      this.finish = true;
      setTimeout(() => {
        this.finish = false;
      }, 1000);
    }

  },
};
</script>
<style scoped>
div {
  padding-top: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  padding-left: 10px;
}
.rounded {
  border-radius: 30px !important;
}
.ligne {
  border-right: solid 1px #95a5a6;
}
.textbox {
  height: 200px;
  border: 1px solid #d3d3d3;
  flex: 1;
  margin: 5px 15px;
  border-radius: 6px;
  text-align: left;
  padding: 16px;
  overflow: auto;
}
.v-progress-circular {
  margin: 1rem;
}
.join-term button {
  margin-right : 15px;
}
</style>
