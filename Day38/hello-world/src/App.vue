<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary p-0">
      <div class="navbar-nav">
        <router-link
          class="nav-item nav-link"
          :class="{ active: current_page == 1 }"
          to="/"
          >Page 1</router-link
        >
        <router-link
          class="nav-item nav-link"
          :class="{ active: current_page == 2 }"
          to="/page2"
          >Page 2</router-link
        >
        <router-link
          class="nav-item nav-link"
          :class="{ active: current_page == 3 }"
          to="/page3"
          >Tab 3</router-link
        >
      </div>

      <ul class="navbar-nav ml-auto">
        <li class="nav-item dropdown no-arrow">
          <a
            class="nav-link dropdown-toggle p-0"
            data-toggle="dropdown"
            href="#"
          >
            <img
              class="rounded-circle"
              style="width: 60px"
              src="https://raw.githubusercontent.com/pytutorial/html_samples/master/css_bootstrap/user.svg"
            />
          </a>
          <div class="dropdown-menu dropdown-menu-right">
            <a class="dropdown-item" href="#"> Thông tin tài khoản </a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#"> Đăng xuất </a>
          </div>
        </li>
      </ul>
    </nav>
    
    <div class="container mt-3">
      <router-view></router-view>
    </div>
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
