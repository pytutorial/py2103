<template>
  <div id="app" class="container mt-3">
    <form id="fmt" @submit.prevent="save()" class="col-9">
      <table class="table">
        <tbody>
          <tr>
            <td><label>Mã:</label></td>
            <td><input class="form-control" name="code" /></td>
          </tr>
          <tr>
            <td><label>Tên:</label></td>
            <td><input class="form-control" name="name" /></td>
          </tr>
        </tbody>
      </table>

      <button class="btn btn-primary">Lưu lại</button>
    </form>
  </div>
</template>
<script>
export default {
  data: () => ({
    name: "",
    baseUrl: 'http://127.0.0.1:8000',
  }),
  methods: {
    save: async function () {
      let data = new FormData(document.getElementById("fmt"));
      console.log(data.get("name"), data.get("code"));
      let url = this.baseUrl + '/api/category/';
      console.log('url=', url);
      fetch(url, {method: 'POST', body: data})
        .then(resp => resp.json())
        .then(result =>{
            if(result.id) {
              this.$router.push('/staff');
            }else{
              console.log('Error:', result);
              alert('Loi xay ra');
            }
        })
    },
  },
  mounted: function () {},
};
</script>
