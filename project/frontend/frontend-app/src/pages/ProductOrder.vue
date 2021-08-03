<template>
  <div class="container mt-5 mb-5">
    <form method="POST" novalidate>
      <h4>Đặt mua hàng trực tuyến</h4>
      <table class="table table-form">
        <tbody>
          <tr>
            <th colspan="2">
              <h5>Thông tin sản phẩm</h5>
            </th>
          </tr>
          <tr>
            <th>Tên sản phẩm:</th>
            <td>Acer 001</td>
          </tr>
          <tr>
            <th>Đơn giá:</th>
            <td>6.500.000 ₫</td>
          </tr>
          <tr>
            <th>Số lượng:</th>
            <td>
              <div style="width: 50px">
                <input class="form-control" type="number" value="1" />
              </div>
            </td>
          </tr>
          <tr>
            <th colspan="2">
              <h5>Thông tin người mua hàng</h5>
            </th>
          </tr>
          <tr>
            <th>Họ và tên:</th>
            <td><input class="form-control" /></td>
          </tr>
          <tr>
            <th>Số điện thoại:</th>
            <td><input class="form-control" /></td>
          </tr>
          <tr>
            <th>Địa chỉ:</th>
            <td><input class="form-control" /></td>
          </tr>
        </tbody>
      </table>
      <a href="thank_you.html" class="btn btn-primary"> Đặt mua </a>
    </form>
  </div>
</template>