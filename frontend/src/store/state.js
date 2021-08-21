// 공통으로 사용할 변수(vuex), 모든곳에서 참조 가능

import { getAuthFromCookie } from "@/utils/cookies";

export default {
    user: {},
    token : getAuthFromCookie() || "",
    id: "",
    
}