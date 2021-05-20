let productList = [
    {code: 'IPX', name: 'IPhone X', price: 12500000},
    {code: 'IP11', name: 'IPhone 11', price: 17500000},
    {code: 'IP12', name: 'IPhone 12', price: 22500000},
];

//TODO:  Nhập vào keyword , priceMin - priceMax
// --> In ra các sản phẩm tên chứa keyword, giá trong khoảng min~max
var n = productList.length;
var minPrice = 5000000;
var maxPrice = 15000000;
var keyword = 'IPhone';

for(var i = 0 ; i < n; i++) {
    var p = productList[i];
    if(p.name.includes(keyword) && p.price > minPrice && p.price < maxPrice) {
        console.log(p.name);
    }
}

productList.filter(p => p.name.includes(keyword))
            .filter(p => p.price > minPrice)
            .filter(p => p.price <  maxPrice)
            .forEach(p => console.log(p.name));

