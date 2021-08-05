<template>
  <div>
    <div class="bg-primary" v-if="$route.path.startsWith('/staff')">
      <div class="container">
        <nav class="navbar navbar-expand navbar-dark bg-primary p-0">
          <ul class="navbar-nav">
            <li class="nav-item" :class="{ active: current_page == 1 }">
              <router-link class="nav-link" to="/staff">Quản lý nhóm sản phẩm</router-link>
            </li>
            <li class="nav-item" :class="{ active: current_page == 2 }">
              <router-link class="nav-link" to="/staff/product">Quản lý sản phẩm</router-link>
            </li>
            <li class="nav-item" :class="{ active: current_page == 3 }">
              <router-link class="nav-link" to="/staff/order">Quản lý đơn hàng</router-link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
    <div class="bg-primary" v-else>
      <div class="container">
        <nav class="navbar navbar-expand navbar-dark bg-primary p-0">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <router-link class="nav-link" to="/">Sản phẩm</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Liên hệ</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  computed:{
    current_page: function() {
        return this.$route.meta.page;
    }
  }
}
</script>