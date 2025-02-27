function solution(a, b) {
    let answer = 0;
    let num1 = a.toString() + b.toString()
    let num2 = b.toString() + a.toString()
    
    return Number(num1) >= Number(num2) ? Number(num1) : Number(num2);
}