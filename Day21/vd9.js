let productList = [
    {code: 'IPX', name: 'IPhone X', price: 12500000},
    {code: 'IP11', name: 'IPhone 11', price: 17500000},
    {code: 'IP12', name: 'IPhone 12', price: 22500000},
];

function printProduct(prod) {
    console.log(prod.code, prod.name, prod.price);
}

var n = productList.length;
for(var i = 0; i < n; i++) {
    printProduct(productList[i]);
}

productList.forEach(p => { 
    console.log(p.code, p.name, p.price);
});
