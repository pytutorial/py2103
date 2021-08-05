<template>
  <div class="container mt-5 mb-5">
    <div class="row">
      <div class="col-6">
        <img
          class="product-detail-image"
          :src="product.image"
        />
      </div>

      <div class="col-6 mt-5">
        <div class="product-detail-title">{{product.name}}</div>
        <br />
        <table class="table">
          <tr>
            <td>Hãng sản xuất:</td>
            <td>{{product.category_name}}</td>
          </tr>
          <tr>
            <td>Giá bán:</td>
            <td><b>{{product.price}} ₫</b></td>
          </tr>
        </table>
        <br />
        <router-link class="btn btn-secondary mr-1" to="/">Quay lại</router-link>
        <router-link class="btn btn-primary" :to="`/order-product/${product.id}`">Mua hàng</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    product: {},
    baseUrl: 'http://127.0.0.1:8000',
  }),
  mounted: async function() {
    //alert(this.$route.params.id);
    const url = this.baseUrl + '/api/product/' + this.$route.params.id;
    console.log('url=', url)
    let resp = await fetch(url);
    this.product = await resp.json();
    console.log(this.product);
  }
}
</script>


<style scoped>
    .product-detail-title {
        font-size: 24px;
        font-weight: bold;
    }

    .product-detail-image {
        width: 100%
    }
</style>