<template>
  <v-app :style="{ background: $vuetify.theme.themes.light.background }">
    <v-layout row>
      <v-flex md3>
        <v-app
          :style="{ background: $vuetify.theme.themes.light.background }"
          style="font-family: 'Jua'"
        >
          <v-container>
            <!-- 상단 설명란 -->
            <v-flex>
              <v-card class="ma-5 text-center mt-10" shaped elevation="10" style="min-width : 400px">
                <v-avatar class="mt-n7" size="80" elevation="10">
                  <v-img src="profile.gif"></v-img>
                </v-avatar>
                <v-card-title class="layout justify-center">
                  {{ user.userName }}
                </v-card-title>
                <v-card-subtitle class="layout justify-center">
                  <div>대구은행</div></v-card-subtitle
                >

                <v-list class="mt-n1">
                  <v-list-item>
                    <v-list-item-title class="cyan--text text--darken-1"
                      >전화번호
                    </v-list-item-title>
                    <v-list-item-title class="cyan--text text--darken-1"
                      >보유 계좌 수</v-list-item-title
                    >
                  </v-list-item>

                  <v-list-item class="mt-n5">
                    <v-list-item-subtitle> {{user.phoneNumber | phone}} </v-list-item-subtitle>
                    <v-list-item-subtitle> {{count}} </v-list-item-subtitle>
                  </v-list-item>
                </v-list>
              </v-card>
            </v-flex>

            <v-flex>
              <v-card
                class="ma-5 mt-n1"
                shaped
                elevation="10"
                style="height: 400px; min-width : 400px; overflow-y : auto"
                
              >
              
                <v-list>
                  <v-list-item>
                    <v-list-item-avatar
                      size="10"
                      color="cyan darken-1"
                    ></v-list-item-avatar>
                    <v-list-item-title class="ml-n1"
                      >보유 계좌 리스트</v-list-item-title
                    >
                  </v-list-item>
                  <v-divider></v-divider>
                </v-list>

                <v-list two-line="" subheader="" style="height: 200px" v-if="count != 0">

                  <v-list v-for="item in myaccount" :key="item.aId">
                  <v-list-item class="layout justify-center">
                    <v-list-item-avatar color="cyan darken-1" size="35">
                      <v-icon dark>fas fa-book</v-icon>
                    </v-list-item-avatar>
                    <v-list-item-content>
                      <v-list-item-title>
                        계좌번호 : {{item.accNum | acc}}
                      </v-list-item-title>
                      <v-list-item-subtitle v-if="item.title == 1"> 대표계좌 </v-list-item-subtitle>
                      <v-list-item-subtitle v-else> 서브계좌 </v-list-item-subtitle>
                    </v-list-item-content>
                      <v-btn v-if="item.title ==0" @click = change(item.accNum)>
                        변경
                      </v-btn>
                  </v-list-item>
                  </v-list>
                </v-list>
                <v-list v-else>
                  <v-list-item style = "margin : 100px 0 0  120px;">
                    <h2>
                      보유 계좌가 없습니다.
                    </h2>
                  </v-list-item>
                </v-list>

              </v-card>
            </v-flex>

            <v-flex>
              <v-card class="ma-5 text-center mt-12" shaped elevation="10" >
              </v-card>
            </v-flex>
            <v-flex>
              <v-card class="ma-5 mt-12" shaped elevation="10" style="min-width : 400px">
                <v-list>
                  <v-list-item>
                    <v-list-item-avatar
                      size="10"
                      color="cyan darken-1"
                    ></v-list-item-avatar>
                    <v-list-item-title class="ml-n2">달력</v-list-item-title>
                  </v-list-item>
                  <v-divider></v-divider>
                </v-list>
                <v-list-item>
                  <v-list-item-content>
                    <v-date-picker color="cyan darken-1">
                    </v-date-picker>
                  </v-list-item-content>
                </v-list-item>
              </v-card>
            </v-flex>
          </v-container>
        </v-app>
      </v-flex>

      <!-- ################################################################################################################################# -->
      <v-flex md9>
        <v-app
          :style="{ background: $vuetify.theme.themes.dark.background }"
          class="rounded"
        >
          <v-container style="font-family: 'Jua'; height: auto">
            <v-flex>
              <!-- #################################### 대표계좌 ########################################################## -->
              <v-row>

                
                <v-col cols="12" md="5" style = "min-width : 450px" v-if="count != 0">
                  <v-list class="mt-5" style="height: 30px">
                    <v-list-item>
                      <v-list-item-avatar
                        color="cyan darken-1"
                        size="20px"
                      ></v-list-item-avatar>
                      <v-list-item-title class="cyan--text text--darken-1">
                        대표 계좌
                      </v-list-item-title>
                    </v-list-item>
                  </v-list>

                  <v-card height = "500" width = "500" style = "margin-top : 50px; border-radius: 30px">
                    <v-col cols="12" md="8" style="margin-left: 50px">
                    
                      <v-list two-line="" subheader="" style="height: 200px" >

                      <v-list-item class="layout justify-center" style = "margin : -20px 0 20px 20px;">
                        <v-card-title>
                          <v-img class="card" src="card2.png"></v-img>
                        </v-card-title>
                      </v-list-item>
                      <v-list-item class="layout justify-center" style = "margin : -20px 0 20px 20px;">
                        <v-card-title>
                        {{mytitleaccount.accNum | acc}}
                        </v-card-title>
                      </v-list-item>
                      <v-list-item class="layout justify-center" style = "margin : -20px 0 20px 20px;">
                        잔고 : {{mytitleaccount.balance | comma}} 원
                      </v-list-item>
                      <v-list-item class="join-term">
                        <v-btn style="width: 30%; margin-right: 20px" to="/remit"
                          >송금</v-btn
                        >
                        <v-btn style="width: 30%; margin-right: 20px" @click="deposit = true"
                          >입금</v-btn
                        >
                        <v-btn style="width: 30%; margin-right: 20px" @click="withdraw = true"
                          >출금</v-btn
                        >
                      </v-list-item>
                      </v-list>
                    </v-col>
                  </v-card>

                </v-col>

                <!--############################ 계좌 없을 경우 ################################ -->
                <v-col cols="12" md="5" style = "min-width : 450px" v-else>
                  
                  <v-list class="mt-5" style="height: 30px">
                    <v-list-item>
                      <v-list-item-avatar
                        color="cyan darken-1"
                        size="20px"
                      ></v-list-item-avatar>
                      <v-list-item-title class="cyan--text text--darken-1">
                        계좌 등록
                      </v-list-item-title>
                    </v-list-item>
                  </v-list>

                  <v-card height = "500" width = "500" style = "margin-top : 50px; border-radius: 30px">
                    <v-col cols="12" md="8" style="margin-left: 50px">
                    
                      <v-list two-line="" subheader="" style="height: 200px" >

                      <v-list-item class="layout justify-center" style = "margin : -20px 0 20px 20px;">
                        <v-card-title>
                          <v-img class="card2" src="card2.png"></v-img>
                        </v-card-title>
                      </v-list-item>
                      <v-list-item class="layout justify-center" style = "margin : -20px 0 20px 20px;">
                        <v-card-title>
                          계좌를 개설하세요!
                        </v-card-title>
                      </v-list-item>
                      
                      <v-list-item class="layout justify-center">
                        <v-btn color="black" to="/account" fab x-large>
                          <v-icon color="white">fas fa-plus</v-icon></v-btn
                        >
                      </v-list-item>
                      </v-list>
                    </v-col>
                  </v-card>
                  <v-col>

                  </v-col>

                </v-col>

                <!-- #################################### 최근 거래내역 ########################################################## -->
                <v-col cols="12" md="6" v-if="count != 0">
                  <v-list class="mt-5" style="height: 30px">
                    <v-list-item>
                      <v-list-item-avatar
                        color="cyan darken-1"
                        size="20px"
                      ></v-list-item-avatar>
                      <v-list-item-title class="cyan--text text--darken-1"
                        >최근 거래내역</v-list-item-title
                      >
                    </v-list-item>
                    <v-list-item v-if="recordFive.length == 5">
                      <v-btn
                        style="width: 20%; margin-left: 20px; margin-top: 20px"
                        to="/trans"
                        >거래내역 조회</v-btn
                      >
                    </v-list-item>
                  </v-list>

                  <v-col cols="12" md="8" style="margin-left: 200px" v-if="recordFive.length != 0">
                    <v-row
                      class="goCal"
                      style="cursor: pointer"
                      v-for="item in recordFive"
                      :key="item"
                    > 
                      <v-col cols="12" md="3">
                        <v-card
                          height="80px"
                          width="10px"
                          color="green"
                          v-if="item[2] == 1"
                        ></v-card>
                        <v-card
                          height="80px"
                          width="10px"
                          color="red"
                          v-else
                        ></v-card>
                      </v-col>
                      <v-col cols="12" md="9" style="width: 80%">
                        <v-list two-line="" subheader="" class="ml-n4">
                          <v-list-item>
                            <v-list-item-content>
                              <v-list-item-subtitle>
                                {{ item[0] }} 
                              </v-list-item-subtitle>
                              <v-list-item-title>
                                {{ item[1] }} 원 ( {{item[3]}} )
                              </v-list-item-title>
                              <v-list-item-subtitle>
                                {{ item[4] }} ( {{item[5]}} 일전 )
                              </v-list-item-subtitle>
                            </v-list-item-content>
                          </v-list-item>
                        </v-list>
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-col v-else>
                    <v-col cols="12" md="8" style="margin-left: 200px; margin-top : 100px;" >
                      <h2>최근 거래내역이 없습니다!</h2>
                          <v-img src="send.gif" style = "width : 60%; height : auto;"></v-img>
                    </v-col>
                  </v-col>

                  <v-col>

                  </v-col>
                </v-col >
                <v-col cols="12" md="5" style = "min-width : 450px" v-else>
                  <v-img src="send.gif" style = "width : 50%; height : auto; margin : 100px 0 0 150px;">

                  </v-img>
                </v-col>


              </v-row>
            </v-flex>

            <v-divider></v-divider>
            <!-- ------------------------------------------------------------------------------- -->

            <v-flex>
              <v-row>
                <v-col cols="12" md="5" v-if="count != 0">
                  <v-flex class="mt-5">
                    <v-list class="ml-5" style="margin-bottom: 30px">
                      <v-list-item>
                        <v-list-item-avatar
                          color="cyan darken-1"
                          size="20px"
                        ></v-list-item-avatar>
                        <v-list-item-title class="cyan--text text--darken-1">
                          주 사용 금액 (일 단위)
                        </v-list-item-title>
                      </v-list-item>
                    </v-list>

                    <div style="text-align: right">단위 : (원)</div>

                    <v-list class="ml-5" style="margin-top: 70px">
                      <v-sparkline
                        :value="dailycount"
                        :gradient="gradient"
                        
                        :padding="8"
                        :line-width="2"
                        
                        
                        :fill="false"
                        
                        
                        auto-draw=""
                      >
                        <template v-slot:label="item">
                          {{ item.value }}
                        </template>
                      </v-sparkline>
                    </v-list>

                    <v-list-item-title
                      class="ml-5"
                      style="margin-top: 70px"
                      align="center"
                      justify="center"
                    >
                        ( {{this.preday }} &emsp;&emsp; &emsp; ~ &emsp;  &emsp;&emsp; {{this.today}} ) 
                    </v-list-item-title>
                  </v-flex>
                </v-col>
                <v-col cols="12" md="5" v-else>
                  <v-img src="main.gif" style = "width : 50%; height : auto; margin : 100px 0 0 100px;">

                  </v-img>
                </v-col>
                <!-- -------------------------------------------------------------------------------------------------- -->

                <v-col cols="12" md="6">
                  <v-flex class="ml-10">
                    <v-list>
                      <v-list-item>
                        <v-list-item-avatar
                          color="cyan darken-1"
                          size="20px"
                        ></v-list-item-avatar>
                        <v-list-item-title class="cyan--text text--darken-1"
                          >상품 소개</v-list-item-title
                        >
                      </v-list-item>
                    </v-list>
                    <v-card
                      elevation="10"
                      style="border-radius: 20px !important"
                    >
                    </v-card>
                  </v-flex>

                  <v-col cols="12" md="12">
                    <v-list-item>
                      <v-carousel
                        cycle
                        height="500"
                        hide-delimiter-background
                        show-arrows-on-hover
                      >
                        <v-carousel-item v-for="img in advertising" :key="img">
                          <v-sheet height="100%">
                            <v-img
                              :src="img.img"
                              style="width 100%; height : auto; margin-left : 20px;"
                            ></v-img>
                            <v-row
                              align="center"
                              justify="center"
                              style="height: 80px; font-size: 20px"
                            >
                              상품명 : {{ img.aName }}
                            </v-row>
                            <v-row align="center" justify="center">
                              {{ img.title }}
                            </v-row>
                          </v-sheet>
                        </v-carousel-item>
                      </v-carousel>
                    </v-list-item>
                  </v-col>
                </v-col>
              </v-row>
            </v-flex>

            <!-- 입출금 모달 -->
            <v-flex>
              <v-row>
                <v-dialog v-model="deposit" persistent max-width="600px">
                  <v-card style="border-radius: 40px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>입금하기</div>
                    </v-card-title>
                    <v-card-text>
                      <v-container>
                        <v-row>
                          <v-col cols="12">
                            <v-select
                              :items="accountList"
                              label="계좌를 선택하세요."
                              v-model="curaccount"
                            ></v-select>
                          </v-col>

                          <v-col cols="12" sm="6" md="5">
                            <v-list-item-title> 보유 현금 : </v-list-item-title>
                          </v-col>
                          <v-col cols="12" sm="6" md="4"> </v-col>
                          <v-col cols="12" sm="6" md="3">
                            <v-list-item-title>
                              {{ user.cash | comma}} 원
                            </v-list-item-title>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-list-item-title> 입금 금액 : </v-list-item-title>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              name="cash"
                              prepend-icon="money"
                              v-model="depositData.cash"
                              placeholder="입금할 금액을 입력해 주세요."
                              text-align:
                              end
                              color="teal accent-3"
                            />
                          </v-col>
                        </v-row>
                      </v-container>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="depositOk = true"
                      >
                        입금
                      </v-btn>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="deposit = false"
                      >
                        닫기
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-row>

              <!-- 입금/출금 완료 -->
              <v-row>
                <v-dialog
                  v-model="depositOk"
                  persistent
                  max-width="300px"
                  height="auto"
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>정말로 입급하시겠습니까?</div>
                    </v-card-title>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="depositOkTrue">
                        입금
                      </v-btn>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="depositOk = false"
                      >
                        닫기
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                <v-dialog
                  v-model="depositClear"
                  persistent
                  max-width="300px"
                  height="300px;"
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>입금 완료!!!!</div>
                    </v-card-title>
                  </v-card>
                </v-dialog>
              </v-row>

              <!-- 출금 -->
              <v-row>
                <v-dialog v-model="withdraw" persistent max-width="600px">
                  <v-card style="border-radius: 40px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>출금하기</div>
                    </v-card-title>
                    <v-card-text>
                      <v-container>
                        <v-row>
                          <v-col cols="12">
                            <v-select
                              :items="accountList"
                              label="계좌를 선택하세요."
                              v-model="curaccount"
                              @change="getFindAccount()"
                            ></v-select>
                          </v-col>

                          <v-col cols="12" sm="6" md="5">
                            <v-list-item-title> 보유 금액 : </v-list-item-title>
                          </v-col>
                          <v-col cols="12" sm="6" md="4"> </v-col>
                          <v-col cols="12" sm="6" md="3">
                            <v-list-item-title>
                              {{ this.withdrawbalance || comma }} 원
                            </v-list-item-title>
                          </v-col>
                          <v-col cols="12" sm="6" style = "font-size : 16px; margin-top : 20px;">
                            출금 금액 : 
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              name="cash"
                              prepend-icon="money"
                              v-model="withdrawData.cash"
                              placeholder="출금할 금액을 입력해 주세요."
                              text-align:
                              end
                              color="teal accent-3"
                            />
                          </v-col>
                          <v-col cols="12" sm="6" style = "font-size : 16px; margin-top : 20px;">
                            비밀번호 : 
                          </v-col>
                          <v-col cols="12" sm="6">
                          <v-text-field
                              name="Password"
                              prepend-icon="lock"
                              placeholder="비밀번호 4자리 입력하세요."
                              type="Password"
                              color="teal accent-3"
                              v-model="password"
                              maxlength='4'
                      />
                          </v-col>
                        </v-row>
                      </v-container>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="withdrawOk = true"
                      >
                        출금
                      </v-btn>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="withdraw = false"
                      >
                        닫기
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-row>
              

              <!-- 출금 완료 -->
              <v-row>
                <v-dialog
                  v-model="withdrawOk"
                  persistent
                  max-width="300px"
                  height="auto"
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>정말로 출금하시겠습니까?</div>
                    </v-card-title>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="withdrawOkTrue">
                        출금
                      </v-btn>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="withdrawOk = false"
                      >
                        닫기
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

                <v-dialog
                  v-model="withdrawClear"
                  persistent
                  max-width="300px"
                  height="300px;"
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div>출금 완료!!!!</div>
                    </v-card-title>
                  </v-card>
                </v-dialog>
              </v-row>


              <!-- ###################### 입/출금 금액 에러 ################## -->

              <v-dialog
                  v-model="depositError"
                  persistent
                  max-width="300px"
                  height="300px;"
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div style ="text-align : center;">보유 현금을 초과했습니다. 다시입력해주세요</div>
                    </v-card-title>
                  </v-card>
                </v-dialog>

              <v-dialog
                  v-model="withdrawError"
                  persistent
                  max-width="300px"
                  height="300px;"
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div style ="text-align : center;">보유 금액을 초과했습니다. 다시입력해주세요</div>
                    </v-card-title>
                  </v-card>
                </v-dialog>

              <v-dialog
                  v-model="pwError"
                  persistent
                  max-width="300px"
                  height="300px;"
                >
                  <v-card style="border-radius: 10px">
                    <v-card-title class="justify-center text--darken-1">
                      <div style ="text-align : center;">비밀 번호가 틀렸습니다... 다시입력해주세요</div>
                    </v-card-title>
                  </v-card>
                </v-dialog>


            </v-flex>


          </v-container>
        </v-app>
      </v-flex>
    </v-layout>
  </v-app>
</template>
<script>
import { mapActions, mapState } from "vuex";
import Filters from "@/utils/filters.js";

const gradients = [
  ["#222"],
  ["#42b3f4"],
  ["red", "orange", "yellow"],
  ["purple", "violet"],
  ["#00c6ff", "#F0F", "#FF0"],
  ["#f72047", "#ffd200", "#1feaea"],
];
export default {
  filters: Filters,
  data() {
    return {
      accountList : [],
      curaccount: "",
      curAccountInfo : [],
      withdrawbalance : 0,
      loading: true,
      myaccount: [],
      curpassword : "",
      password : "",
      depositError : false,
      withdrawError : false,
      pwError : false,
      depositData: {
        id: "",
        cash: "",
      },
      withdrawData: {
        id: "",
        cash: "",
      },
      count : 0,
      gradient: gradients[5],
      value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
      mywrite: [],
      mylastwrite: [],
      mytitleaccount : [],
      dailycount: [],
      today : "",
      preday : "",
      daily: [],
      deposit: false,
      depositOk: false,
      depositClear: false,
      withdraw: false,
      withdrawOk : false,
      withdrawClear : false,
      imgs: [
        { name: "입금 하기", icon: "input" },
        { name: "출금 하기", icon: "credit_card" },
        { name: "송금 하기", icon: "send" },
        { name: "내역 보기", icon: "list" },
      ],
      colors: ["#B6D1F6", "#B6D1F6", "#B6D1F6", "#B6D1F6"],
      
      recent: ["3", "1", "2", "2", "4"],
      advertising: [],

      recordMoney : 0,
      recordType : 0,
      recordFive : [],
        
      

    };
  },
  created() {
    this.getUserinfo();
    this.getCount();
    this.getAlladver();
  },

  computed: {
    ...mapState({
      user: "user",
    }),
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
  },
  methods: {
    ...mapActions([
      "USERINFO",
      "GET_FETCHCOUNT",
      "GET_FETCHMYACCOUNT",
      "GET_FETCHWEEK",
      "GET_FETCHFINDACCOUNT",
      "PUT_RECORD",
      "GET_TRADEFIVE",
      "GET_ALLADVER",
      "PUT_CHANGEACCOUNT",
      ]),

    getUserinfo() {
      this.USERINFO().then(() => {
        console.log(this.user);
        
      });
    },
    async getCount() {
      await this.GET_FETCHCOUNT().then((response) => {
        this.count = response.data.count;
      })

      if(this.count != 0) {
        this.getMyAccount();
        this.getTitleAccount();
      }
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

    async getTitleAccount() {
      let type = 1;
      await this.GET_FETCHMYACCOUNT(type).then((response) => {
        this.mytitleaccount = response.data;
        this.getWeek(this.mytitleaccount.accNum);
        
        this.tradeFive(this.mytitleaccount.accNum);
        this.withdrawbalance = this.mytitleaccount.balance;
        
      })
    },

    depositOkTrue() {
      if(this.checkMoney(this.depositData.cash, 1)) {
        this.depositOk = false;
        this.deposit = false;
        this.depositClear = true;
        setTimeout(() => {
          this.depositClear = false;
        }, 1000);
        // 맞을 경우 돈 반영하기
        this.recordMoney = this.depositData.cash;
        this.recordType = 1;
        this.goRecord();
      }else{
        this.depositOk = false;
      }
    },
    withdrawOkTrue() {
      console.log(this.password + " " + this.curpassword);
      if(this.password != this.curpassword) {
        this.pwError = true;
        this.withdrawOk = false;
        setTimeout(() => {
          this.pwError = false;
        }, 1000);
        return;
      }

      if(this.checkMoney(this.withdrawData.cash, 2)){
        this.withdrawOk = false;
        this.withdraw = false;
        this.withdrawClear = true;
        setTimeout(() => {
          this.withdrawClear = false;
        }, 1000);
        // 맞을 경우 돈 반영하기
        this.recordMoney = this.withdrawData.cash;
        this.recordType = 2;
        this.goRecord();
      }else{
        this.withdrawOk = false;
      }
    },
    async getWeek(value) {
      
      await this.GET_FETCHWEEK(value).then((response) => {
        
        this.dailycount = response.data[0];
        this.preday = response.data[1];
        this.today = response.data[2];
      })
    },
    async getFindAccount() {
      await this.GET_FETCHFINDACCOUNT(this.curaccount).then((response) => {
        this.curAccountInfo = response.data;
        this.withdrawbalance = response.data[0].balance;
        this.curpassword = response.data[0].password;
      })
      console.log(this.curAccountInfo);
    },
    
    checkMoney(value, type) {
      // 1 : 입금, 2 : 출금
      if(type == 1) {
        if(value > this.user.cash) {
          this.depositError = true;
          setTimeout(() => {
          this.depositError = false;
          }, 1000);
          return false;
        }
      }else{
        if(value > this.withdrawbalance) {
          this.withdrawError = true;
          setTimeout(() => {
          this.withdrawError = false;
          }, 1000);
          return false;
        }
      }
      return true;
    },
    // 입/출금 내역 저장하기
    async goRecord() {
      let recordData = {
        accNum : this.curaccount,
        money : this.recordMoney,
        type : this.recordType
      };
      console.log(recordData.accNum + " " + recordData.money + " " + recordData.type);

      await this.PUT_RECORD(recordData).then(() => {
        
      })
      this.$router.go();
    },
    // 최근 거래내역 5개 가져오기
    async tradeFive(value) {
      
      await this.GET_TRADEFIVE(value).then((response) => {
        this.recordFive = response.data;
      })
      
    },
    // 광고 가져오기
    async getAlladver() {
      await this.GET_ALLADVER().then((response) => {
        this.advertising = response.data;
      })
    },

    async change(accNum){
      await this.PUT_CHANGEACCOUNT(accNum).then(() => {
        console.log(accNum);
      })
      alert("변경 완료!");
      this.$router.go();
    }
  },
};
</script>
<style scoped>
.rounded {
  border-top-left-radius: 50px !important;
  border-bottom-left-radius: 50px !important;
}
.goCal:hover {
  transform: scale(1);
  box-shadow: 1px 1px 6px 1px rgba(0, 0, 0, 0.3);
}

.join-term button {
  width: 50%;
  margin-right: 20px;
}

.card {
  max-width: 100%;
  height: auto;
  margin-top: 50px;
  animation: watch 1s linear infinite both;
}

@keyframes watch {
  0% {
    transform: translate(0);
  }

  40% {
    transform: translate(-5px, -5px);
  }

  80% {
    transform: translate(5px, -5px);
  }
  100% {
    transform: translate(0);
  }
}


.card2 {
  max-width: 100%;
  height: auto;
  margin-top: 50px;
  animation: watch2 1s linear infinite both;
}

@keyframes watch2 {
  

  40% {
    transform: translate(-5px, -5px);
  }

  
  100% {
    transform: translate(0);
  }
}

</style>
