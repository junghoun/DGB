// 백엔드 통신(axios)
import axios from 'axios';
import { setInterceptors } from "./common/interceptors"

function createInstance() {
    return axios.create({
        baseURL : process.env.VUE_APP_API_URL,
    });
}



function createInstanceWithAuth(url) {
    const instance = axios.create({
      baseURL: `${process.env.VUE_APP_API_URL}${url}`,
    });
    return setInterceptors(instance);
 }

export const instance = createInstance();
export const count = createInstanceWithAuth("count");
export const users = createInstanceWithAuth("user");
export const myaccount = createInstanceWithAuth("myaccount");
export const findaccount = createInstanceWithAuth("findaccount");
export const oneaccount = createInstanceWithAuth("oneaccount");
export const trade = createInstanceWithAuth("trade");
export const week = createInstanceWithAuth("week");
export const record = createInstanceWithAuth("record");
export const adver = createInstanceWithAuth("adver");
export const date = createInstanceWithAuth("date");
export const account = createInstanceWithAuth("account");
export const card = createInstanceWithAuth("card");


//  < create - posts / post - posts / put - posts {id} / delete - posts {id} >