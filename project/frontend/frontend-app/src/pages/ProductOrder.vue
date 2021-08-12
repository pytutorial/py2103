<template>
  <div class="container mt-5 mb-5">
    <form id="fmt" @submit.prevent="orderProduct()" method="POST" novalidate>
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
            <td>{{product.name}}</td>
          </tr>
          <tr>
            <th>Đơn giá:</th>
            <td>{{product.price}} ₫</td>
          </tr>
          <tr>
            <th>Số lượng:</th>
            <td>
              <div style="width: 50px">
                <input name="qty" class="form-control" type="number" value="1" />
              </div>
              <span style="color:red" v-if="errors.qty">{{errors.qty[0]}}</span>
            </td>
          </tr>
          <tr>
            <th colspan="2">
              <h5>Thông tin người mua hàng</h5>
            </th>
          </tr>
          <tr>
            <th>Họ và tên:</th>
            <td>
              <input name="customerName" class="form-control" />
              <span style="color:red" v-if="errors.customerName">{{errors.customerName[0]}}</span>
            </td>
          </tr>
          <tr>
            <th>Số điện thoại:</th>
            <td>
              <input name="customerPhone" class="form-control" />
              <span style="color:red" v-if="errors.customerPhone">{{errors.customerPhone[0]}}</span>
            </td>
          </tr>
          <tr>
            <th>Địa chỉ:</th>
            <td>
              <input name="customerAddress" class="form-control" />
              <span style="color:red" v-if="errors.customerAddress">{{errors.customerAddress[0]}}</span>
            </td>
          </tr>
        </tbody>
      </table>
      <button type="submit" class="btn btn-primary">Đặt mua</button>
    </form>
  </div>
</template>
<script>
export default {
  data: () => ({
    product: {},
    errors: {},
    baseUrl: 'http://127.0.0.1:8000'
  }),
  methods: {
    orderProduct: async function() {
      let data = new FormData(document.getElementById('fmt'));
      let id = this.$route.params.id;
      let resp = await fetch(this.baseUrl +'/api/order-product/'+id, {body:data, method:'POST'});
      if(resp.ok){ // 200
        this.$router.push('/thank-you');
      }else {
        this.errors = await resp.json();
      }
    }
  },
  mounted: async function() {
    let id = this.$route.params.id;
    let resp = await fetch(this.baseUrl + '/api/product/' + id);
    this.product = await resp.json();
    console.log(this.product);
  }
}
</script>
