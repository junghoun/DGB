// 회원정보 확인, 수정, 삭제
import { users } from "./index";

function getUserinfo() {
  return users.get("/info/");
}
function updateUserinfo({ name, major, minor }) {
  return users.put("/info/", { name: name, major: major, minor: minor });
}

export { getUserinfo, updateUserinfo};
