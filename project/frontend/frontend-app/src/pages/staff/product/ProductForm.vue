<template>
  <div id="app" class="container mt-3">
    <form id="fmt" @submit.prevent="save()" class="col-9">
      <table class="table">
        <tbody>
          <tr>
            <th style="width:30%">Nhóm sản phẩm:</th>
            <td>
              <select class="form-control" name='category' v-model="item.category">
                <option value=''>----Chọn nhóm sản phẩm----</option>
                <option v-for="(c,i) in categoryList" :key="i" :value="c.id">
                  {{c.name}}
                </option>
              </select>

              <span style="color:red" v-if="errors.category">{{errors.category[0]}}</span>
            </td>
          </tr>
          <tr>
            <th><label>Mã:</label></th>
            <td>
              <input class="form-control" name="code" v-model="item.code"/>
              <span style="color:red" v-if="errors.code">{{errors.code[0]}}</span>
            </td>
          </tr>
          <tr>
            <th><label>Tên:</label></th>
            <td>
              <input class="form-control" name="name" v-model="item.name"/>
              <span style="color:red" v-if="errors.name">{{errors.name[0]}}</span>
            </td>
          </tr>
          <tr>
            <th><label>Mô tả:</label></th>
            <td>
              <textarea class="form-control" name="description" v-model="item.description"></textarea>
              <span style="color:red" v-if="errors.description">{{errors.description[0]}}</span>
            </td>
          </tr>
          <tr>
            <th><label>Đơn giá:</label></th>
            <td>
              <input type="number" style="max-width:150px" class="form-control" name="price" v-model="item.price"/>
              <span style="color:red" v-if="errors.price">{{errors.price[0]}}</span>
            </td>
          </tr>
          <tr>
            <th><label>Ảnh:</label></th>
            <td>
              <input type="file" class="form-control-file" name="image" />
              <a class="mt-1" target="_blank" v-if="item.image" :href="item.image">
                <small>Ảnh đã upload</small><br/>
              </a>
              <span style="color:red" v-if="errors.image">{{errors.image[0]}}</span>
            </td>
          </tr>
        </tbody>
      </table>
      <router-link to="/staff/product" class="btn btn-secondary mr-2">Quay lại</router-link>
      <button class="btn btn-primary">Lưu lại</button>
    </form>
  </div>
</template>
<script>
export default {
  data: () => ({
    baseUrl: 'http://127.0.0.1:8000',
    name: "",
    errors: {},
    item:{},
    categoryList:[]
  }),
  methods: {
    save: async function () {
      let url;
      let method;

      let data = new FormData(document.getElementById("fmt"));
    
      if(this.item.id) {         //update
        url = this.baseUrl + `/api/product/${this.item.id}/`;
        method = "PUT";
      }else{                    //create
        url = this.baseUrl + '/api/product/';
        method = "POST";
      }
      
      console.log('url=', url);

      let headers = {'Authorization': 'Bearer ' + window.localStorage.getItem('access_token')};
      let resp = await fetch(url, {method: method, body: data, headers });
      if(resp.ok) {
        this.$router.push('/staff/product');
      }else{
        let result = await resp.json();
        this.errors = result;
        console.log('errors=', result);
      }
    },
  },
  mounted: async function () {
    let resp = await fetch(this.baseUrl+'/api/category');
    this.categoryList = await resp.json()
    
    let id = this.$route.params.id;
    if(id){
      resp = await fetch(this.baseUrl + '/api/product/' + id);
      this.item = await resp.json();
    }
  },
};
</script>
