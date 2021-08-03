<template>
  <div class="container mt-5 mb-5">
    <div class="row">
      <div class="col-6">
        <img
          class="product-detail-image"
          src="https://raw.githubusercontent.com/pytutorial/themes/master/shop_themes/images/sample.jpg"
        />
      </div>

      <div class="col-6 mt-5">
        <div class="product-detail-title">Acer 001</div>
        <br />
        <table class="table">
          <tr>
            <td>Hãng sản xuất:</td>
            <td>Acer</td>
          </tr>
          <tr>
            <td>Giá bán:</td>
            <td><b>6.500.000 ₫</b></td>
          </tr>
        </table>
        <br />
        <router-link class="btn btn-secondary mr-1" to="/">Quay lại</router-link>
        <router-link class="btn btn-primary" to="/order-product/1">Mua hàng</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
    .product-detail-title {
        font-size: 24px;
        font-weight: bold;
    }

    .product-detail-image {
        width: 100%
    }
</style>