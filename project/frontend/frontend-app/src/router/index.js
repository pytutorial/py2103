//src/router/index.js
import Vue from "vue";
import VueRouter from "vue-router";
import ProductList from "../pages/ProductList";
import ProductDetail from "../pages/ProductDetail";

Vue.use(VueRouter);
const router = new VueRouter({
    routes: [
        {path:'/' , component: ProductList, meta:{page:1}},
        {path: '/view-product', component: ProductDetail, meta:{page:2}},
    ]
});
export default router;