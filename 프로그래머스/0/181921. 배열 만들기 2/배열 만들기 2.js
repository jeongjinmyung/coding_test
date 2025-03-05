function solution(l, r) {
    const answer = [];
    
    for (let i=l; i<=r; i++) {
        if ([...String(i)].every(value => value === '5' || value === '0')) {
            answer.push(i);
        }
    }
    return answer.length > 1 ? answer : [-1];
}