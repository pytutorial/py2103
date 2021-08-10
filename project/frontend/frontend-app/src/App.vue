<template>
  <div>
    <div v-if="$route.path.startsWith('/staff')">
      <navbar-staff></navbar-staff>
    </div>
    <div v-else>
      <navbar-user></navbar-user>
    </div>
    <router-view></router-view>
  </div>
</template>
<script>
import NavbarStaff from './components/NavbarStaff.vue';
import NavbarUser from './components/NavbarUser.vue';

export default {
  components: {NavbarStaff, NavbarUser},

  computed:{
    current_page: function() {
        return this.$route.meta.page;
    }
  }
}
</script>