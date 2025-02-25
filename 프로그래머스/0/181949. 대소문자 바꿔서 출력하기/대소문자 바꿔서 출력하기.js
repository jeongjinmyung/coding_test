const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    let str = input[0];
    let arr = str.split('');
    arr = arr.map(function(v) {
        return v === v.toUpperCase() ? v.toLowerCase() : v.toUpperCase();
    });
    console.log(arr.join(''));
});