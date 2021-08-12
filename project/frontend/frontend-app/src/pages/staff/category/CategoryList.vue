<template>
  <div id="app" class="container mt-3">
    <div class="row">
      <div class="col">
        <router-link to="/staff/category/create" class="btn btn-primary float-right">
          Thêm nhóm sản phẩm
        </router-link>
      </div>
    </div>

    <table class="table table-bordered mt-3">
      <thead>
        <tr>
          <th style="width: 10%">STT</th>
          <th style="width: 35%">Mã</th>
          <th style="width: 40%">Tên</th>
          <th style="width: 15%"></th>
        </tr>
      </thead>
      <tbody v-if="!loading">
        <tr v-if="items.length==0">
          <td colspan="4">Không có nhóm sản phẩm nào</td>
        </tr>
        <tr v-for="(c, i) in items" :key="i">
          <td class="text-center">{{ i + 1 }}</td>
          <td>{{ c.code }}</td>
          <td>{{ c.name }}</td>
          <td>
            <button @click="deleteItem(c.id)" class="btn btn-sm btn-danger">Xoá</button>
            <router-link :to="`/staff/category/update/${c.id}`" class="ml-2 btn btn-sm btn-secondary">
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
    baseUrl: "http://127.0.0.1:8000",
  }),
  methods: {
    deleteItem: async function(id){
      if(!confirm('Bạn có chắc muốn xoá nhóm này?')){
        return;
      }
      let url = this.baseUrl + `/api/category/${id}/`;
      console.log('url=', url);
      let headers = {'Authorization': 'Bearer ' + window.localStorage.getItem('access_token')};
      let resp = await fetch(url, {method: 'DELETE', headers});
      if(resp.ok) {
        this.fetch_data();
      }else{
        alert('Lỗi xảy ra');
      }
    },

    fetch_data: async function () {
      this.loading = true;
      let resp = await fetch(this.baseUrl + "/api/category");
      this.items = await resp.json();
      this.loading = false;
      console.log(this.items);
    },
  },
  mounted: async function () {
    this.fetch_data();
  },
};
</script>
