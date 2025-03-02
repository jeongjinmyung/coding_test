function solution(a, b, c) {
    const sum = a + b + c
    const sumSeq = a**2 + b**2 + c**2
    const sumCub = a**3 + b**3 + c**3
    
    if (a === b && b === c) {
        return sum * sumSeq * sumCub;
    } else if (a === b || b === c || a === c) {
        return sum * sumSeq;
    } else {
        return sum;
    }
}