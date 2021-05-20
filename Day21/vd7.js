// Vd7 : Cho 1 dãy số (phân biệt),
// in ra các bộ (a,b,c) trong dãy số : a + b = c
var lst = [1, 2, 4, 6, 17, 9 , 15, 8];

n = lst.length
for(var i = 0; i < n; i++) {
    for(var j = 0; j < n; j++) {
        var x = lst[i];
        var y = lst[j];
        if(i < j && lst.includes(x + y)){
            console.log(x, y, x+y);
        }
    }
}