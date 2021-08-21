import {trade} from "./index";

function fetchTrade({sender, receiver, money}) {
    return trade.put("/", {sender : sender, receiver : receiver, money : money});
}

function fetchAddTrade({sender, receiver, money}) {
    return trade.put("/add/", {sender : sender, receiver : receiver, money : money});
}

export {fetchTrade, fetchAddTrade}