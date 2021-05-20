// Vd6 : Cho 1 dãy số, in ra tổng dãy số đó 
var lst = [1, 5, 7, 4, 6, 3, 5, 7 ];
let sum = 0;
let n = lst.length;
for(var i = 0; i < n; i++) {
    sum += lst[i];
}
console.log(sum);