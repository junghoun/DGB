// state를 변경시키는 역할(동기 처리)
export default {
    setToken(state, token){
        state.token = token;
    },
    clearToken(state){
        state.token = "";
    },
    SET_USER(state, data){
        state.user = data;
    },
    
}