import { findaccount, oneaccount, account} from "./index";

function fetchFindaccount(value) {
    return findaccount.get(`/?value=${value}`);
}

function fetchOneaccount(value) {
    return oneaccount.get(`/?value=${value}`);
}

function fetchAddaccount({type, password}) {
    return account.post("/add/", {type: type, password : password});
}

function changeAccount(accNum) {
    return account.put("/change/", {accNum : accNum});
}

export { fetchFindaccount, fetchOneaccount, fetchAddaccount, changeAccount};
