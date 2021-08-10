<template>
  <div class="bg-login">
    <div class="login-form">
      <h3>Đăng nhập</h3>
      <br>
      <form id="fmt" @submit.prevent="logIn()">
        <div class="form-group">
          <label>Tên tài khoản</label>
          <input name="username" type="text" class="form-control" />
        </div>
        <div class="form-group">
          <label>Mật khẩu</label>
          <input name="password" type="password" class="form-control" />
        </div>
        <div class="form-group">
          <span id="error" style="color:red">{{error}}</span>
        </div>
        <br>
        <div class="form-group">
          <button type="submit" class="btn btn-primary btn-block">Đăng nhập</button>
        </div>
        <div class="clearfix">
          <a href="#" class="float-right">Quên mật khẩu?</a>
        </div>
      </form>
      <p class="text-center"><a href="#">Đăng ký tài khoản</a></p>
    </div>
  </div>
</template>

<script>
export default{
  data: () => ({
    baseUrl: 'http://127.0.0.1:8000',
    error: ''
  }),
  methods: {
    logIn: async function() {
      let data = new FormData(document.getElementById('fmt'));
      let resp = await fetch(this.baseUrl + '/api/token',
                        {method: 'POST', body: data});
      let result = await resp.json();
      
      if(!result.access){
        this.error = 'Tên đăng nhập/mật khẩu không đúng';
      }else {
        window.localStorage.setItem('access_token', result.access);
        window.location.reload();
      }
    }
  }
}
</script>

<style scoped>
  .bg-login {
    position: relative;
    width: 100%;
    min-height: auto;
    background-position: right 0px top 0px;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    background-size: cover;
    -o-background-size: cover;
  }

  .login-form {
    border: 1px solid #DDD;
    max-width: 400px;
    padding: 20px;
    margin-top: 100px;
    margin-left: 30%;
  }
</style>