// map ~ list comprehension
var lst = [1, 2, 3, 4, 7, 6, 5];

//function square(x) {
//    return x*x;
//}
//var lst2 = lst.map(square);
var lst2 = lst.map(x => x*x);
console.log(lst2);

// filter ~ if in list comprehension
//lst3 = [x*x for x in lst if x%2==0]
var lst3 = lst.filter(x => x%2==0)
                .map(x => x*x);

console.log(lst3);

// find ~ find one
let x = lst.find(it => it > 5);
console.log(x);

// some ~ any
// every ~ all