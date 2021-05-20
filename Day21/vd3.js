var ho_ten = 'Nguyễn Văn A';
var items = ho_ten.split(' ');
var n = items.length;
console.log('Họ :', items[0]);
console.log('Tên:', items[n-1]);
console.log('Tên đệm:', items.slice(1,n-1).join(' '));