//src/router/index.js
import Vue from "vue";
import VueRouter from "vue-router";
import ProductList from "../pages/ProductList";
import ProductDetail from "../pages/ProductDetail";

import ProductOrder from "../pages/ProductOrder"; // TODO: Them file src/pages/ProductOrder.vue
import ThankYou from "../pages/ThankYou";  // TODO: Them file src/pages/ThankYou.vue
Vue.use(VueRouter);
const router = new VueRouter({
    routes: [
        {path:'/' , component: ProductList, meta:{page:1}},
        {path: '/view-product', component: ProductDetail, meta:{page:2}},
        {path: '/order-product', component: ProductOrder, meta:{page:3}},
        {path: '/thank-you', component: ThankYou, meta:{page:4}},
    ]
});
export default router;