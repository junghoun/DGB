// front 화면 이동
import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store/index";

Vue.use(VueRouter);

const router = new VueRouter({
    mode : "history",
    base : process.env.BASE_URL,
    routes: [
        {
            path: "/",
            redirect : "/home",
        },
        {
            path: "/login",
            component: () => import("@/views/LoginPage.vue"),
        },
        {
            path: "/signup",
            component: () => import("@/views/SignUpPage.vue"),
        },
        {
            path: "/homePage",
            component: () => import("@/views/HomePage.vue"),
            meta: { auth: true },
        },
        {
            path: "/home",
            component: () => import("@/views/Home.vue"),
            
        },
        {
            path: "/adver",
            component: () => import("@/views/Adver.vue"),
            meta: { auth: true },
        },
        {
            path: "/remit",
            component: () => import("@/views/Remit.vue"),
            meta: { auth: true },
        },
        {
            path: "/trans",
            component: () => import("@/views/Trans.vue"),
            meta: { auth: true },
        },
        {
            path: "/account",
            component: () => import("@/views/Account.vue"),
            meta: { auth: true },
        },
    ]
});

router.beforeEach((to, from, next) => {
    if(to.meta.auth && ! store.getters.isLogin) {
        next("/login");
        return;
    }
    next();
});

export default router;