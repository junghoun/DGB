import {week} from "./index";

function fetchWeek(value) {
    return week.get(`/?value=${value}`);
}

export { fetchWeek };