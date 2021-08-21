<template>
  <v-app :style="{ background: $vuetify.theme.themes.light.background }" style="font-family:'Jua';">
       
    <v-container>
      <v-layout>

        <v-app style="background-color: grey lighten-1;" class="rounded mx-auto">

          <v-row style="font-family:'Jua';">
            <v-col cols="12" md="8" class="ligne">
              <v-container>
                <v-row>
                  
                  <v-col cols="12" md="12" align="center" justify="center">
                    <v-card
                      elevation="10"
                      style="border-radius: 30px !important; height : 250px;"
                    >
                      <v-list>
                        <v-list-item>
                          <v-list-item-title class="headline font-weight-bold">
                            계좌 정보
                          </v-list-item-title>
                        </v-list-item>
                         <v-divider class="mx-4"></v-divider>
                        <v-list-item>
                          <v-list-item-title class="ml-n1">
                            계좌번호 : {{mytitleaccount.accNum | acc}}
                          </v-list-item-title>
                          
                        </v-list-item>
                        <v-list-item class = "layout justify-center ml-n3 mt-n7">
                              잔액 : {{mytitleaccount.balance | comma}} 원
                          </v-list-item>
                      </v-list>
                      

                      
                      <v-list-item three-line="">
                      </v-list-item>
                      
                    </v-card>

                    <v-list style = "margin-top : 50px;">
                      <v-card-text class="headline font-weight-bold">
                        송금 정보
                      </v-card-text>
                      
                      <v-text-field prepend-icon="search" placeholder="받는사람 이름, 또는 계좌번호" 
                      type="text" color="teal accent-3" style = "width :60%;" v-model="check" @keyup.enter="getFindAccount">
                      </v-text-field>
                      <v-list>
                      <v-list-item style = "margin-bottom : 50px;">    
                        <v-list-item-title class="cyan--text text--darken-1">
                            계좌번호 
                        </v-list-item-title>
                        <v-list-item-title v-if="receivaccount.length ==0"></v-list-item-title>
                        <v-list-item-title class="text--darken-1" v-else>
                            {{receivaccount.accNum | acc}}
                        </v-list-item-title>
                      </v-list-item>

                      <v-divider class="mx-4"></v-divider>
                      <v-list-item style = "margin-bottom : 50px;">    
                        <v-list-item-title class="cyan--text text--darken-1">
                            보내는사람 
                        </v-list-item-title>
                        <v-list-item-title v-if="receivaccount.length ==0"></v-list-item-title>
                        <v-list-item-title class="text--darken-1" v-else>
                            {{user.userName}}
                        </v-list-item-title>
                      </v-list-item>
                      <v-divider class="mx-4"></v-divider>
                      <v-list-item style = "margin-bottom : 50px;">    
                        <v-list-item-title class="cyan--text text--darken-1">
                            받는사람
                        </v-list-item-title>
                        <v-list-item-title v-if="receivaccount.length ==0"></v-list-item-title>
                        <v-list-item-title class="text--darken-1" v-else>
                            {{ receivaccount.ownerName}}
                        </v-list-item-title>
                      </v-list-item>

                      </v-list>
                    </v-list>
                    
                    
                    <v-text-field prepend-icon="money" :disabled="!nice"
                     placeholder="금액을 입력하세요" type="number" style = "width : 40%" v-model="money"
                     :rules="[rules.required]" />
                    

                    <v-btn
                      :disabled="!valid"
                      color="cyan"
                      class="field-submit"
                      @click="resultflag"
                    >확인 -></v-btn>
                    
                  </v-col>
                </v-row>
              </v-container>
            </v-col>
            






            <v-col cols="12" md="4" align="center" justify="center" style="font-family:'Jua'; ">
              <v-row>
                
                <v-col cols="12" md12>
                  <v-card color="#D9D9D9" style = "margin-top : 50px;">
                    <v-card-title>
                      <v-spacer></v-spacer>
                      <v-icon large left>send</v-icon>
                      <span class="title">내 통장</span>
                    </v-card-title>

                    <v-card-text class="headline font-weight-bold" style = "margin-top : 50px; margin-bottom : 50px;">
                      {{ mytitleaccount.ownerName}} ({{mytitleaccount.accNum | acc}})
                    </v-card-text>

                    
                  </v-card>

                  <v-divider></v-divider>
                  <v-card color="#C0F2CA" style = "margin-top : 100px; height : 230px;">
                    <v-card-title>
                      <v-spacer></v-spacer>
                      <v-icon large left>dvr</v-icon>
                      <span class="title">받는 통장</span>
                    </v-card-title>

                    <v-card-text class="headline font-weight-bold" style = "margin-top : 50px; margin-bottom : 50px;" v-if="receivaccount.length != 0">
                      {{receivaccount.ownerName}} ({{receivaccount.accNum | acc}})
                    </v-card-text>

                    
                  </v-card>
                </v-col>
                
                <v-col>
                  <v-divider></v-divider>
                </v-col>
                <v-col cols="12" md12>
                  <v-card class="mx-auto" width="400" height="250" style = "margin-top : 100px;">
                    <v-card-text class="headline font-weight-bold">송금 정보</v-card-text>
                    
                    <div v-if="result.length != 0">
                    <v-card-text>
                        받는사람 : {{result.receive_name}} ({{result.receive_accNum}})
                    </v-card-text>
                    <v-card-text>
                        금액 : {{result.money | comma}} 원
                    </v-card-text>
                    <v-card-text style = "margin-bottom : 0px;">
                        일시 : {{result.trade_date}}
                    </v-card-text >
                    
                    <v-btn depressed large color="black white--text" @click="pwcheck = true">
                      <v-icon left small>email</v-icon>
                        <spen>송금하기</spen>
                    </v-btn>
                    </div>
                  </v-card>

                </v-col>
                
              </v-row>

              <!-- 리스트 조회 팝업창 -->
              <v-row>
                <v-dialog v-model="checkflag" persistent max-width="600px" >
                  <v-card style="border-radius: 40px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>계좌 리스트</div>
                    </v-card-title>
                    <v-divider></v-divider>
                    
                    <v-card-text v-if="checklist.length == 0">
                      <v-container class="justify-center text--darken-1" style = "height : 250px;">
                        <div style = "font-weight : bold; font-size : 20px; text-align : center; margin-top : 100px;">
                          검색 결과가 없습니다.
                        </div>
                      </v-container>
                    </v-card-text>
                    <v-card-text v-else style="height: 350px; overflow-y: auto;">
                      <v-container class="justify-center text--darken-1" style = "height : 200px;">
                        <v-row v-for="item in checklist" :key="item.accNum" elevation="10"
                        class= "goAcc" style="cursor: pointer; " @click="getAccount(item.accNum)">
                          <v-list >
                            <v-list-item class="layout justify-center">
                            <v-list-item-avatar color="cyan darken-1" size="35">
                              <v-icon dark>fas fa-book</v-icon>
                            </v-list-item-avatar>
                              <v-list-item-content>
                              <v-list-item-title>
                                계좌번호 : {{item.accNum | acc}}
                              </v-list-item-title>
                                <v-list-item-subtitle> {{item.ownerName}} </v-list-item-subtitle>
                              </v-list-item-content>
                            </v-list-item>
                          </v-list>
                        </v-row>
                      </v-container>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="checkflag = false"
                      >
                        닫기
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-row>


              <!-- 비밀번호 입력 -->
              <v-row>
                <v-dialog v-model="pwcheck" persistent max-width="600px" >
                  <v-card style="border-radius: 40px" align="center" justify="center">
                    <v-card-title class="justify-center text--darken-1">
                      <div>비밀번호 입력</div>
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-text-field
                      name="finishpw"
                      prepend-icon="lock"
                      placeholder="비밀번호 4자리 입력하세요."
                      type="Password"
                      color="teal accent-3"
                      style="width : 50%;"
                      maxlength='4'
                      v-model="finishpw"
                      
                      />
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="FinalCheck()"
                      >
                        송금
                      </v-btn>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="pwcheck = false"
                      >
                        닫기
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

                <!-- 비밀번호 틀렸을 때 -->
                <v-dialog
                  v-model="pwBad"
                  persistent
                  max-width="330px"
                  height="auto"
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>비밀번호가 틀렸습니다!!</div>
                    </v-card-title>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="pwBad = false"
                      >
                        닫기
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                <v-dialog
                  v-model="finishflag"
                  persistent
                  max-width="300px"
                  height="300px;"
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>송금 완료!!!!</div>
                    </v-card-title>
                  </v-card>
                </v-dialog>
              </v-row>


            </v-col>
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
      mytitleaccount : [],
      receivaccount : [],
      result : [],
      check : "",
      checklist : [],
      checkflag : false,
      valid: false,
      nice : false,
      pwcheck : false,
      pwBad : false,
      finishflag : false,
      bal : 0,
      money : 0,
      finishpw : "",
      rules: {
        required: (value) => {
          if(value >= this.bal || value < 0) {
            
            this.valid = false
            
          }else{
            this.valid = true;
          }
          
        }
      },
    };
  },
  computed: {
    ...mapState({
      user: "user",
      dialog : "dialog",
    }),
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
  },
  created() {
    this.getUserinfo();
    this.getTitleAccount();
    
  },
  
  methods: {
    ...mapActions([
      "USERINFO",
      "GET_FETCHMYACCOUNT",
      "GET_FETCHFINDACCOUNT",
      "GET_FETCHONEACCOUNT",
      "PUT_TRADE",
      "ADD_TRADE",
      ]),
    
    getUserinfo() {
      this.USERINFO().then(() => {
        console.log(this.user);
        
      });
    },
    async getTitleAccount() {
      let type = 1;
      await this.GET_FETCHMYACCOUNT(type).then((response) => {
        this.mytitleaccount = response.data;
        this.bal = this.mytitleaccount.balance;
      })
    },

    async getFindAccount() {
      await this.GET_FETCHFINDACCOUNT(this.check).then((response) => {
        this.checklist = response.data;
      }),
      this.checkflag = true;
    },
    
    async getAccount(value) {
      await this.GET_FETCHONEACCOUNT(value).then((response) => {
        this.receivaccount = response.data;
      })
      this.checkflag = false;
      this.nice = true;
    },
    resultflag() {
      let today = new Date();
      let date = today.getFullYear() + '-' + (today.getMonth()+1) + "-" + today.getDate() + ' ' + today.getHours() + ":" + today.getMinutes();
      this.result = {"send_accNum" : this.mytitleaccount.accNum, "send_name" : this.mytitleaccount.ownerName, "receive_accNum" : this.receivaccount.accNum,
      "receive_name" : this.receivaccount.ownerName, "money" : this.money, "trade_date" : date, "comment" : ""};
      console.log(this.result);
    },
    
    FinalCheck() {
      console.log(this.finishpw + " " + this.mytitleaccount.password);
      if(this.finishpw == this.mytitleaccount.password) {
        this.pwGood = true;
        this.goTrade();
      }else{
        this.pwBad = true;
      }
    },
    async goTrade() {
      let tradeData = {
        sender : this.mytitleaccount.accNum,
        receiver : this.receivaccount.accNum,
        money : this.money
      };
      console.log(tradeData.sender + " " + tradeData.receiver + " " + tradeData.money);
      await this.PUT_TRADE(tradeData).then(() => {
        this.pwcheck = false;
        this.finishflag = true;
        this.addTrade();
        setTimeout(() => {
        this.finishflag = false;
        this.getTitleAccount();
      }, 1000);
      })
      
    },
    
    async addTrade() {
      let tradeData = {
        sender : this.mytitleaccount.accNum,
        receiver : this.receivaccount.accNum,
        money : this.money
      };
      await this.ADD_TRADE(tradeData).then(() => {
        console.log("거래 내역 저장 완료.");
      })
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

.goAcc:hover {
  transform: scale(1);
  box-shadow: 1px 1px 6px 1px rgba(0, 0, 0, 0.3);
}
</style>
