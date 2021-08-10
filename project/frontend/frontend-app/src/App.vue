<template>
  <div>
    <div v-if="$route.path.startsWith('/staff')">
      <div v-if="access_token">
        <navbar-staff :current_page="current_page"></navbar-staff>
        <router-view></router-view>
      </div>
      <log-in v-else></log-in>
    </div>
    <div v-else>
      <navbar-user></navbar-user>
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
import NavbarStaff from './components/NavbarStaff.vue';
import NavbarUser from './components/NavbarUser.vue';
import LogIn from './components/LogIn.vue';

export default {
  components: {NavbarStaff, NavbarUser, LogIn},

  computed:{
    current_page: function() {
      return this.$route.meta.page;
    },
    access_token: function() {
      return window.localStorage.getItem('access_token');
    }
  }
}
</script>