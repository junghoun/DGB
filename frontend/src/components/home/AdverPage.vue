<template>
  <v-app :style="{ background: $vuetify.theme.themes.light.background }" style="font-family:'Jua';">
       
    <v-container class="cont">
      <v-layout>

        <v-app style="background-color: grey lighten-1;" class="rounded mx-auto">

          <v-row style="font-family:'Jua';">
            
              <v-container>
                <v-row style = "width = 2000px;">
                  
                  <v-col cols="12" md="12" align="center" justify="center">
                    <v-card
                      elevation="10"
                      style="border-radius: 40px !important; height : auto; width : 1000px;"
                    >
                      <v-list>
                        <v-list-item>
                          <v-list-item-title class="headline font-weight-bold">
                            상품몰
                          </v-list-item-title>
                        </v-list-item>
                         <v-divider class="mx-4" style = "display : flex;"></v-divider>
                        <v-list-item>
                          <div style = "width : 500px;">
                            상품 선택 :
                          </div>
                          <v-list-item >
                            <v-select label="상품명 선택" style="width : 40%"
                            :items="titleList"
                            v-model="curadver"
                            @change="getAdver(curadver)"
                            ></v-select>
                          </v-list-item>
                          
                          <div style = "width : 300px;">

                          </div>
                        </v-list-item>
                        <v-list-item>
                          <div style = "width : 500px;">
                            상품명 : 
                          </div>
                          <v-list-item class="join-term">
                            <h1>{{advertising.aName}}</h1>
                          </v-list-item>
                          
                          <div style = "width : 300px;">
                            
                          </div>
                        </v-list-item>
                        <v-list-item>
                          <div style = "width : 500px;">
                            상품 요약설명 : 
                          </div>
                          <v-list-item>
                            {{advertising.title}}
                          </v-list-item>
                          
                          <div style = "width : 300px;">
                            
                          </div>
                        </v-list-item>
                        
                        <v-list-item >
                          <v-btn style="margin : auto;" color="black white--text">
                            <v-icon left small>search</v-icon>
                              <spen @click="show">상세 내용</spen>
                          </v-btn>
                        </v-list-item>
                      </v-list>
                      
                    </v-card>

                    

                    <v-list v-if="flag">
                      <v-row>
                        <v-col cols="12" md="1"></v-col>
                        <v-col cols="12" md="6">

                          

                          <v-card >
                            <v-img
                                :src="advertising.img"
                                style="width : 700px; height : 300px;"
                              ></v-img>
                          </v-card>
                        </v-col>
                        <v-col cols="12" md="4">
                          <v-card style = "width : 300px; height : 320px;">
                                <h1 style = "margin-top : 50px; margin-bottom : 50px;">
                                    {{advertising.aName}}
                                </h1>
                                <h3>
                                {{advertising.title}}
                                </h3>
                          </v-card>
                        </v-col>
                        

                      </v-row>

                      <v-row>
                        <v-col cols="12" md="1"></v-col>
                        <v-col cols="12" md="10">
                            <v-img
                                :src="advertising.contents"
                                style=" height : 250px;"
                              ></v-img>
                        </v-col>
                      </v-row>
                      
                            
                      
                      

                      
                    </v-list>  
                    
                    
                    
                    
                  </v-col>
                </v-row>

              </v-container>
            
            
           
          </v-row>
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
      
     adverList : [],
     titleList : [],
     curAdver : "",
     advertising : [],
     flag : false,
      
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
    this.getAlladver();
  },
  
  methods: {
    ...mapActions([
      "USERINFO",
      "GET_ALLADVER",
      "GET_GETADVER",
      ]),
    
    getUserinfo() {
      this.USERINFO().then(() => {
        console.log(this.user);
        
      });
    },
    
    async getAlladver() {
      
      await this.GET_ALLADVER().then((response) => {
        this.adverList = response.data;
        for(var i = 0; i < response.data.length; i++) {
          this.titleList.push(response.data[i].aName);
        }
      })
    },

    async getAdver(value) {
      await this.GET_GETADVER(value).then((response) => {
        this.advertising = response.data;
      })
      console.log(this.advertising)
    },

    show() {
      this.flag = true;
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
