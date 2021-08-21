import { adver} from "./index";

function fetchGetadver(value) {
    return adver.get(`/get/?value=${value}`);
}

function fetchAlladver() {
    return adver.get(`/all/`);
}

export { fetchGetadver, fetchAlladver};
