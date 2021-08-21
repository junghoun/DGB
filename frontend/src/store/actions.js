// mutations 실행하는 역할(비동기 처리)
import axios from "axios";

import { getUserinfo} from "@/api/user";
import { loginUser } from "@/api/auth";
import { fetchCount } from "@/api/count";
import {saveAuthToCookie, deleteCookie} from "@/utils/cookies";
import { fetchMyaccount } from "@/api/myaccount";
import { fetchFindaccount, fetchOneaccount, fetchAddaccount, changeAccount } from "@/api/account";
import {fetchTrade, fetchAddTrade} from "@/api/trade";
import {fetchWeek} from "@/api/week";
import {fetchRecord, fetchFive, getList} from "@/api/record";
import { fetchAlladver, fetchGetadver } from "../api/adver";
import { fetchDate } from "../api/date";

export default {
    // 로그인
    async LOGIN({commit}, userData) {
        const {data} = await loginUser(userData);
        axios.defaults.headers.common["token"] = `${data.token}`;
        commit("setToken", data.token);
        saveAuthToCookie(data.token);
        return data;

    },
    // 로그아웃
    LOGOUT({commit}) {
        commit("clearToken"),
        deleteCookie("til_auth");
        delete axios.defaults.headers.common["token"];
    },
    //회원정보 가져오기
    USERINFO({ commit }) {
        return getUserinfo()
          .then((response) => {
            commit("SET_USER", response.data);
          })
          .catch(() => {
            console.log("회원정보오류");
          });
    },

    // 계좌 수 가져오기
    GET_FETCHCOUNT() {
      return fetchCount();
    },

    //내 계좌 정보 가져오기
    GET_FETCHMYACCOUNT(_, type) {
      return fetchMyaccount(type);
    },

    //원하는 계좌 결과 가져오기
    GET_FETCHFINDACCOUNT(_, value) {
      return fetchFindaccount(value);
    },

    //원하는 계좌 결과 가져오기
    GET_FETCHONEACCOUNT(_, value) {
      return fetchOneaccount(value);
    },

    // 거래 결과 양쪽에 반영
    PUT_TRADE(_, {sender, receiver, money}) {
      return fetchTrade({sender, receiver, money}).then(() => {});
    },


    // 거래 결과 저장
    ADD_TRADE(_, {sender, receiver, money}) {
      return fetchAddTrade({sender, receiver, money}).then(() => {});
    },


    GET_FETCHWEEK(_, value) {
      return fetchWeek(value);
    },

    // 입/출금 결과 반영
    PUT_RECORD(_, {accNum, money, type}) {
      return fetchRecord({accNum, money, type}).then(() => {});
    },

    //전체 광고 가져오기
    GET_ALLADVER() {
      return fetchAlladver();
    },

    // 해당 광고 가져오기
    GET_GETADVER(_, value){
      return fetchGetadver(value);
    },


    GET_TRADEFIVE(_, value) {
      return fetchFive(value);
    },

    // 날짜 가져오기
    GET_DATE(_, value) {
      return fetchDate(value);
    },

    // 계좌 등록
    INSERT_ACCOUNT(_, {type, password}) {
      return fetchAddaccount({type, password}).then(() => {});
    },

    //메인 계좌 변경
    PUT_CHANGEACCOUNT(_, accNum) {
      return changeAccount(accNum).then(() => {});
    },


    //거래 결과 가져오기
    GET_LIST(_, { accNum, day }) {
      return getList({ accNum, day });
    },

}