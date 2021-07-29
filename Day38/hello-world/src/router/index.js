import Vue from "vue";
import VueRouter from "vue-router";
import Page1 from "../pages/Page1";
import Page2 from "../pages/Page2";
import Page3 from "../pages/Page3";

Vue.use(VueRouter);
const router = new VueRouter({
    routes: [
        {path:'/' , component: Page1,     meta:{page:1}},
        {path: '/page2', component: Page2, meta:{page:2}},
        {path: '/page3', component: Page3, meta:{page:3}},
    ]
});
export default router;