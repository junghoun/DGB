<template>
  <v-app :style="{ background: $vuetify.theme.themes.light.background }" style="font-family:'Jua';">
       
    <v-container class="cont">
      <v-layout>

        <v-app style="background-color: grey lighten-1;" class="rounded mx-auto">

          <v-row style="font-family:'Jua';">
            
              <v-container>
                <v-row>
                  
                  <v-col cols="12" md="12" align="center" justify="center">
                    <v-card
                      elevation="10"
                      style="border-radius: 40px !important; height : auto; width : 1000px;"
                    >
                      <v-list>
                        <v-list-item>
                          <v-list-item-title class="headline font-weight-bold">
                            거래내역 조회
                          </v-list-item-title>
                        </v-list-item>
                         <v-divider class="mx-4" style = "display : flex;"></v-divider>
                        <v-list-item>
                          <div style = "width : 500px;">
                            계좌번호 :
                          </div>
                          <v-list-item>
                            <h2>
                            {{this.mytitleaccount.accNum | acc}}
                            </h2>
                          </v-list-item>
                          
                          <div style = "width : 300px;">

                          </div>
                        </v-list-item>
                        <v-list-item>
                          <div style = "width : 500px;">
                            조회기간 : 
                          </div>
                          <v-list-item class="join-term">
                            <v-btn @click = setDate(0)>당일</v-btn>
                            <v-btn @click = setDate(3)>3일</v-btn>
                            <v-btn @click = setDate(7)>일주일</v-btn>
                            <v-btn @click = setDate(30)>한달</v-btn>
                            <v-btn @click = setDate(180)>6개월</v-btn>
                            <v-btn @click = setDate(365)>일년</v-btn>
                          </v-list-item>
                          
                          <div style = "width : 300px;">

                          </div>
                        </v-list-item>
                        <v-list-item style="text-align: center; margin: -20px 270px ">
                            
                          <v-list-item>
                            <v-text-field
                              
                              solo
                              dense
                              :value = date[0]
                              disabled
                            ></v-text-field>
                          </v-list-item>
                          <p>~</p>
                          <v-list-item >
                            <v-text-field
                              
                              solo
                              dense
                              :value = date[1]
                              disabled
                            ></v-text-field>
                          </v-list-item>

                        </v-list-item>
                        <v-list-item >
                          <v-btn style="margin : auto;" color="black white--text">
                            <v-icon left small>search</v-icon>
                              <spen @click = "searchRecord">조회하기</spen>
                          </v-btn>
                        </v-list-item>
                      </v-list>
                      
                    </v-card>

                    <v-list v-if="!flag">
                      

                    </v-list>
                    <v-list v-else>


                      <v-list style = "margin-top : 50px;">
                        <v-card-text class="headline font-weight-bold">
                          조회 결과
                        </v-card-text>
                      </v-list>

                      <v-list v-if="this.resultCnt == 0" style = "margin-top : 100px;">
                        <h1>
                        거래내역이 없습니다!!
                        </h1>
                      </v-list>
                      <v-list v-else>
                        <v-list v-for="item in showList" :key="item" style = "padding : 0 0 0 0;">                      

                          <v-list-item-title style = "text-align : left; width:70%;"> 
                              {{item[4]}} ( {{item[5]}} 일전)
                              <v-spacer></v-spacer>                    
                              {{item[0]}}

                          </v-list-item-title>
                          <v-list v-if="item[2] == '1'">      
                              <v-list-item-subtitle  style = "color : blue; text-align : right; width:70%;">
                                입금 {{item[1] | comma}} 원 
                              </v-list-item-subtitle>
                          </v-list>
                          <v-list v-else>
                            <v-list-item-subtitle  style = "color : red; text-align : right; width:70%;"> 
                                출금 {{item[1] | comma}} 원 </v-list-item-subtitle>
                          </v-list>

                          <v-divider style = "width : 70%"></v-divider>
                        </v-list>

                        <v-list>
                          <v-btn :disabled="pageNum == 0" @click ="prevPage">
                            이전
                          </v-btn>
                          <span> &emsp;{{pageNum +1}} / {{pageCount}} page &emsp;</span>
                          <v-btn :disabled="pageNum >= pageCount -1" @click="nextPage">
                            다음
                          </v-btn>
                        </v-list>
                      </v-list>
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
import Filters from "@/utils/filters.js";


export default {
  filters: Filters,
  data() {
    return {
    
     flag : false,
     accountList : [],
     myaccount : [],
     curaccount : [],
     date : [],
     dateValue : 0,
     mytitleaccount : [],
     resultCnt : 0,
     resultList : "",
     ShowList : "",


     // paging 관련
     pageNum : 0,
     pageCount : 1,

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
    this.getMyAccount();
    this.getDate(0);
    this.getTitleAccount(1);
  },
  
  methods: {
    ...mapActions([
      "USERINFO",
      "GET_FETCHMYACCOUNT",
      "GET_DATE",
      "GET_LIST",
      ]),
    
    getUserinfo() {
      this.USERINFO().then(() => {
        console.log(this.user);
        
      });
    },
    async getMyAccount() {
      let type = 2;
      await this.GET_FETCHMYACCOUNT(type).then((response) => {
        this.myaccount = response.data;
        for(var i = 0; i < response.data.length; i++) {
          this.accountList.push(response.data[i].accNum);
        }
      })
    },
    async getDate(value) {
      
      await this.GET_DATE(value).then((response) => {
        this.date = response.data;  
      })
      
    },

    setDate(value) {
      this.dateValue = value;
      this.getDate(value);
    },
    // 조회
    async searchRecord() {
      let data = {
        accNum : this.mytitleaccount.accNum,
        day : this.dateValue,
        
      };
      this.GET_LIST(data).then((response) => {
        this.resultList = response.data.results;
        this.resultCnt = response.data.cnt;
        this.pageCount = Math.floor(this.resultCnt / 5);
        this.checkList(0, 5)
      });
      this.pageNum = 0;
      this.flag = true;
      
            
    },

    async getTitleAccount() {
      let type = 1;
      await this.GET_FETCHMYACCOUNT(type).then((response) => {
        this.mytitleaccount = response.data;
      })
      console.log(this.mytitleaccount)
    },

    // paging 관련
    nextPage() {
      this.pageNum +=1;
      let page = (this.pageNum * 5)
      this.checkList(page, page+5)
    },
    prevPage() {
      this.pageNum -=1;
      let page = (this.pageNum * 5)
      this.checkList(page, page+5)
    },
    checkList(start, end) {
      this.showList = this.resultList.slice(start, end)
      console.log(this.showList)
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
