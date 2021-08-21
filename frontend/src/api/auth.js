// 로그인, 회원가입
import { instance} from "./index";

// 회원가입
function registerUser(userData) {
    return instance.post("user/join/", userData);
}

// 로그인
function loginUser(userData) {
    return instance.post("user/login/", userData);
}

// 비밀번호 찾기
function findPw(userData) {
    return instance.post("user/findpw/", userData);
}

export {registerUser, loginUser, findPw};