// then이나 catch 처리되기 전에 요청 응답 가로채기
import store from "@/store/index";

export function setInterceptors(instance) {
    instance.interceptors.request.use(
        function(config){
            config.headers.token = store.state.token;
            return config;
        },
        function(error) {
            return Promise.reject(error);
        }
    );

    instance.interceptors.response.use(
        function(response){
            return response;
        },
        function(error){
            return Promise.reject(error);
        }
    );
    return instance;
}

