function solution(a, d, included) {
    let answer = 0;
    let n = included.length;
    
    for (let i = 0; i < n; i++) {
        if (included[i]) {
            answer += a + (i * d);
        }
    }
    
    return answer;
}