import { myaccount } from "./index";

function fetchMyaccount(type) {
  return myaccount.get(`/?type=${type}`);
}



export { fetchMyaccount };
