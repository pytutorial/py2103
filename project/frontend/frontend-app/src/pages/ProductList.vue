<template>
  <div class="container mt-5 mb-5">
    <div class="row">
      <div class="col-3 p-3 card">
        <form>
          <div class="product-search-info mt-3">
            <label><b>Tên sản phẩm</b></label>
            <input
              name="name"
              class="form-control"
              placeholder="Nhập tên sản phẩm để tìm"
            />
          </div>

          <div class="category-search-info mt-3">
            <label><b>Hãng sản xuất:</b></label>
            <div>
              <input type="radio" name="categoryId" checked value="" />
              <label>Tất cả</label>
            </div>
            <div v-for="(c,i) in categoryList" :key="i">
              <input  name="categoryId" type="radio" :value="c.id" />
              <label>{{c.name}}</label>
            </div>
          </div>

          <div class="price-search-info mt-3">
            <label><b>Mức giá:</b></label>
            <div>
              <input type="radio" name="priceRange" checked value="" />
              <label>Tất cả</label>
            </div>

            <div>
              <input type="radio" name="priceRange" value="1" />
              <label>Dưới 10 triệu</label>
            </div>

            <div>
              <input type="radio" name="priceRange" value="2" />
              <label>Từ 10-20 triệu</label>
            </div>

            <div>
              <input type="radio" name="priceRange" value="3" />
              <label>Trên 20 triệu</label>
            </div>
          </div>

          <button type="submit" class="btn btn-primary mt-3">Tìm kiếm</button>
        </form>
      </div>
      <div class="col-9">
        <ul class="list-unstyled row">
          <li v-for="(p,i) in items" :key="i" class="list-item col-sm-4 mt-3" >
            <div class="item-container">
              <router-link :to="`view-product/${p.id}`" class="product-item">
                <img
                  :src="p.image"
                  class="product-image"
                />
                <div class="item-info">
                  <div>
                    <span class="product-name">{{p.name}}</span>
                  </div>
                  <div>
                    <span class="price-title">Giá bán :</span>
                    <span class="price">{{p.price}} ₫</span>
                  </div>
                </div>
              </router-link>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    data: () => ({
      categoryList:[],
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
          //TODO: Fetch categoryList
          resp = await fetch(this.baseUrl+'/api/category');
          this.categoryList = await resp.json()
          console.log(this.categoryList);
        }
    },
    mounted: async function(){
        this.fetch_data()
    }
}
</script>

<style scoped>
.product-image {
  width: 95%;
}

.price-title {
  font-style: italic;
  font-size: 14px;
}

.price {
  font-size: 16px;
  font-weight: bold;
}

.product-item,
.product-item:link,
.product-item:hover,
.product-item:visited {
  text-decoration: none;
  color: black;
}

.item-container {
  position: relative;
  height: 100%;
  padding-bottom: 50px;
}

.item-info {
  position: absolute;
  bottom: 0px;
  height: 50px;
}
</style>
