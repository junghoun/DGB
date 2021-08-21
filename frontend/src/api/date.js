import { date } from "./index";

function fetchDate(value) {
    return date.get(`/?value=${value}`);
}

export { fetchDate };
