<template>
  <div id="app" class="container mt-3">
    <div class="row">
      <div class="col">
        <router-link to="/staff/product/create" class="btn btn-primary float-right">
          Thêm sản phẩm 
        </router-link>
      </div>
    </div>
    <table class="mt-3 table table-bordered">
      <thead>
        <tr>
          <th style="width:5%">STT</th>
          <th style="width:15%">Mã</th>
          <th style="width:20%">Tên</th>
          <th style="width:15%">Đơn giá</th>
          <th style="width:30%">Ảnh</th>
          <th style="width:15%">Ảnh</th>
        </tr>
      </thead>
      <tbody v-if="!loading">
        <tr v-if="items.length==0">
          <td colspan="6">Không có sản phẩm nào</td>
        </tr>
        <tr v-for="(p,i) in items" :key="i">
          <td class="text-center">{{i+1}}</td>
          <td>{{p.code}}</td>
          <td>{{p.name}}</td>
          <td class="text-center">{{p.price}} ₫</td>
          <td><img style="max-width:100%; max-height:200px" :src="p.image" /></td>
          <td>
            <button @click="deleteItem(p.id)" class="btn btn-sm btn-danger">Xoá</button>
            <router-link :to="`/staff/product/update/${p.id}`" class="ml-2 btn btn-sm btn-secondary">
              Cập nhật
            </router-link>
          </td>
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
        loading: true,
        pageSize: 5,
        baseUrl: 'http://127.0.0.1:8000'
    }),
    methods: {
      fetch_data: async function(){
        this.loading = true;
        let resp = await fetch(this.baseUrl+'/api/product');
        this.items = await resp.json();
        console.log(this.items);
        this.loading = false;
      },
      
      deleteItem: async function(id){
        if(!confirm('Bạn có chắc muốn xoá sản phẩm này?')){
          return;
        }
        let url = this.baseUrl + `/api/product/${id}/`;
        console.log('url=', url);
        let headers = {'Authorization': 'Bearer ' + window.localStorage.getItem('access_token')};
        let resp = await fetch(url, {method: 'DELETE', headers});
        if(resp.ok) {
          this.fetch_data();
        }else{
          alert('Lỗi xảy ra');
        }
      },
    },
    mounted: async function(){
      this.fetch_data()
    }
}
</script>
