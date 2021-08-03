<template>
  <div>
    <div class="bg-primary">
      <div class="container">
        <nav class="navbar navbar-expand navbar-dark bg-primary p-0">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="#">Sản phẩm</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Liên hệ</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>

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
              <div>
                <input name="categoryId" type="radio" value="1" />
                <label>Acer</label>
              </div>
              <div>
                <input name="categoryId" type="radio" value="2" />
                <label>Asus</label>
              </div>
              <div>
                <input name="categoryId" type="radio" value="3" />
                <label>Lenovo</label>
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
            <li class="list-item col-sm-4 mt-3">
              <div class="item-container">
                <a href="view_product.html?id=1" class="product-item">
                  <img
                    src="https://raw.githubusercontent.com/pytutorial/themes/master/shop_themes/images/sample.jpg"
                    class="product-image"
                  />
                  <div class="item-info">
                    <div>
                      <span class="product-name">Acer 001</span>
                    </div>
                    <div>
                      <span class="price-title">Giá bán :</span>
                      <span class="price">6.500.000 ₫</span>
                    </div>
                  </div>
                </a>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

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
