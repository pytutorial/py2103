<template>
  <div class="bg-primary">
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
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a href='javascript:void(0)' @click="logOut()" class="nav-link">Đăng xuất</a>
          </li>
        </ul>
      </nav>
    </div>
  </div>  
</template>
<script>
export default{
  props: ['current_page'],
  methods: {
    logOut: function() {
      window.localStorage.removeItem('access_token');
      window.location.reload();
    }
  }
}
</script>