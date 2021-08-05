//src/router/index.js
import Vue from "vue";
import VueRouter from "vue-router";
import ProductList from "../pages/ProductList";
import ProductDetail from "../pages/ProductDetail";

import ProductOrder from "../pages/ProductOrder"; // TODO: Them file src/pages/ProductOrder.vue
import ThankYou from "../pages/ThankYou";  // TODO: Them file src/pages/ThankYou.vue

import CategoryList from "../pages/staff/category/CategoryList";
import CategoryForm from "../pages/staff/category/CategoryForm";
import ProductListStaff from "../pages/staff/product/ProductList";
import ProductForm from "../pages/staff/product/ProductForm";
import OrderList from "../pages/staff/order/OrderList";
import OrderDetail from "../pages/staff/order/OrderDetail";

Vue.use(VueRouter);
const router = new VueRouter({
    routes: [
        {path:'/' , component: ProductList, meta:{page:1}},
        {path: '/view-product/:id', component: ProductDetail, meta:{page:2}},
        {path: '/order-product/:id', component: ProductOrder, meta:{page:3}},
        {path: '/thank-you', component: ThankYou, meta:{page:4}},

        // Category
        {path: '/staff', component: CategoryList, meta:{page:1}},
        {path: '/staff/category/create', component: CategoryForm, meta:{page:1}},
        {path: '/staff/category/update/:id', component: CategoryForm, meta:{page:1}},

        // Product
        {path: '/staff/product', component: ProductListStaff, meta:{page:2}},
        {path: '/staff/product/create', component: ProductForm, meta:{page:2}},
        {path: '/staff/product/update/:id', component: ProductForm, meta:{page:2}},

        // Order
        {path: '/staff/order', component: OrderList, meta:{page:3}},
        {path: '/staff/order/detail/:id', component: OrderDetail, meta:{page:3}},
    ]
});
export default router;