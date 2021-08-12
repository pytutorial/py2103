<template>
  <div id="app" class="container mt-3">
    <form id="fmt" @submit.prevent="save()" class="col-9">
      <table class="table">
        <tbody>
          <tr>
            <th style="width:30%">Mã:</th>
            <td>
              <input v-model="item.code" class="form-control" name="code" />
              <span style="color:red" v-if="errors.code">{{errors.code[0]}}</span>
            </td>
          </tr>
          <tr>
            <th>Tên:</th>
            <td>
              <input v-model="item.name" class="form-control" name="name" />
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
    item: {},
  }),
  methods: {
    save: async function () {
      let url;
      let method;

      let data = new FormData(document.getElementById("fmt"));
      if(this.item.id) {             //update
        url = this.baseUrl + `/api/category/${this.item.id}/`;
        method = "PUT";
      }else{                    //create
        url = this.baseUrl + '/api/category/';
        method = "POST";
      }
      
      console.log('url=', url); 
      let headers = {'Authorization': 'Bearer ' + window.localStorage.getItem('access_token')};
      let resp = await fetch(url, {method: method, body: data, headers:headers});
      if(resp.ok){
        this.$router.push('/staff');
      }else{
        let result = await resp.json();
        console.log('Error:', result);
        this.errors = result;
      }
    },
  },
  mounted: async function () {
    let id = this.$route.params.id;
    if(id){
      let resp = await fetch(this.baseUrl + '/api/category/' + id);
      this.item = await resp.json();
    }
  },
};
</script>
