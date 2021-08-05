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
          <th style="width: 40%">Mã</th>
          <th style="width: 50%">Tên</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(c, i) in items" :key="i">
          <td class="text-center">{{ i + 1 }}</td>
          <td>{{ c.code }}</td>
          <td>{{ c.name }}</td>
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
    baseUrl: "http://127.0.0.1:8000",
  }),
  methods: {
    fetch_data: async function () {
      let resp = await fetch(this.baseUrl + "/api/category");
      this.items = await resp.json();
      console.log(this.items);
    },
  },
  mounted: async function () {
    this.fetch_data();
  },
};
</script>
