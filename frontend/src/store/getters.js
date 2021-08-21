// 각 컴포넌트의 계산된 속성(computed)의 공통 사용 정의

export default {
    authorized: (state) => !!state.token,
    authstatus: (state) => state.authstatus,
    isLogin(state) {
        return state.token != "";
    },
};