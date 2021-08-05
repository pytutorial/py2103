<template>
  <div id="app" class="container mt-3">
    <div class="row">
      <div class="col">
        <a href="product_form.html" class="btn btn-primary float-right"
          >Thêm sản phẩm</a
        >
      </div>
    </div>
    <table class="mt-3 table table-bordered">
      <thead>
        <tr>
          <th style="width:5%">STT</th>
          <th style="width:20%">Mã</th>
          <th style="width:25%">Tên</th>
          <th style="width:20%">Đơn giá</th>
          <th style="width:30%">Ảnh</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(p,i) in items" :key="i">
          <td class="text-center">{{i+1}}</td>
          <td>{{p.code}}</td>
          <td>{{p.name}}</td>
          <td class="text-center">{{p.price}} ₫</td>
          <td><img style="max-width:100%; max-height:200px" :src="p.image" /></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
    data: () => ({
        keyword: "",
        page: 1,
        total: 0,
        items: [],
        pageSize: 5,
        baseUrl: 'http://127.0.0.1:8000'
    }),
    methods: {
        fetch_data: async function(){
          let resp = await fetch(this.baseUrl+'/api/product');
          this.items = await resp.json();
          console.log(this.items);
        }
    },
    mounted: async function(){
        this.fetch_data()
    }
}
</script>
