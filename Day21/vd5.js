// Vd5 : In ra các số có 2 chữ số mà tổng 2 chữ số = 9
for(var i = 1; i < 10; i++) {
    for(var j = 0; j < 10; j++) {
        if(i+j == 9){
            console.log(`${i}${j}`);
        }
    }
}