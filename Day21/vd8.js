var product = {
    code: 'IPX',
    name: 'IPhone X',
    price: 12500000
};

console.log(product['code'], product.name);

let productList = [
    {code: 'IPX', name: 'IPhone X', price: 12500000},
    {code: 'IP11', name: 'IPhone 11', price: 17500000},
    {code: 'IP12', name: 'IPhone 12', price: 22500000},
];

var n = productList.length;
for(var i = 0; i < n; i++) {
    var prod = productList[i];
    console.log(`${prod.code}\t${prod.name}\t${prod.price}`);
}