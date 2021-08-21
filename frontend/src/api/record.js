import {record} from "./index";

function fetchRecord({accNum, money, type}) {
    return record.put("/", {accNum : accNum, money : money, type : type});
}

function fetchFive(value) {
    return record.get(`/tradefive/?value=${value}`);
}

function getList({ accNum, day }) {
    return record.get(`/list/?accNum=${accNum}&day=${day}`);
  }

export {fetchRecord, fetchFive, getList}