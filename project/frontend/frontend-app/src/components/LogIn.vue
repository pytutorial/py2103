<template>
  <div class="bg-login">
    <div class="login-form">
      <h3>Đăng nhập</h3>
      <br>
      <form method="POST">
        <div class="form-group">
          <label>Tên tài khoản</label>
          <input name="username" type="text" class="form-control" />
        </div>
        <div class="form-group">
          <label>Mật khẩu</label>
          <input name="password" type="password" class="form-control" />
        </div>
        <div class="form-group">
          <span id="error" style="color:red"></span>
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