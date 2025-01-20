const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);
let A = input[0]
let B = input[1]

if (A > B){
    console.log(">");
} else if (A < B){
    console.log("<");
} else{
    console.log("==");
}