var productList = [
    {code: 'IPX', name: 'IPhone X'},
    {code: 'IP11', name: 'IPhone 11'},
    {code: 'IP12', name: 'IPhone 12'},
];

var orders = [
    {productCode: 'IPX', qty: 2, date: '2021-05-18'},
    {productCode: 'IP11', qty: 1, date: '2021-05-19'},
    {productCode: 'IP12', qty: 1, date: '2021-05-20'},
];

var n = orders.length;
for(var i = 0; i < n; i++) {
    var order = orders[i];
    /*
    var p = null;
    for(var j = 0; j < productList.length; j++) {
        if(productList[j].code == order.productCode) {
            p = productList[j];
            break;
        }
    }*/
    var p = productList.find(prod => prod.code == order.productCode);
    order.productName = p ? p.name : ""; // p.name if p else ''
}

// =======
orders.forEach(o => {
    var p = productList.find(prod => prod.code == o.productCode);
    o.productName = p? p.name : "";
});
console.log(orders);