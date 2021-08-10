<template>
  <div id="app" class="container mt-3">
    <form id="fmt" @submit.prevent="save()" class="col-9">
      <table class="table">
        <tbody>
          <tr>
            <td><label>Mã:</label></td>
            <td>
              <input class="form-control" name="code" />
              <span style="color:red" v-if="errors.code">{{errors.code[0]}}</span>
            </td>
          </tr>
          <tr>
            <td><label>Tên:</label></td>
            <td>
              <input class="form-control" name="name" />
              <span style="color:red" v-if="errors.name">{{errors.name[0]}}</span>
            </td>
          </tr>
        </tbody>
      </table>
      <router-link to="/staff" class="btn btn-secondary mr-2">Quay lại</router-link>
      <button class="btn btn-primary">Lưu lại</button>
    </form>
  </div>
</template>
<script>
export default {
  data: () => ({
    name: "",
    baseUrl: 'http://127.0.0.1:8000',
    errors: {},
  }),
  methods: {
    save: async function () {
      let data = new FormData(document.getElementById("fmt"));
      let url = this.baseUrl + '/api/category/';
      
      console.log('url=', url);
      let resp = await fetch(url, {method: 'POST', body: data});
      let result = await resp.json();

      if(result.id) {
        this.$router.push('/staff');
      }else{
        console.log('Error:', result);
        this.errors = result;
        //alert('Loi xay ra');
      }
    },
  },
  mounted: function () {},
};
</script>
