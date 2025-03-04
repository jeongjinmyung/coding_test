function solution(arr, queries) {
    const checker = (arr, s, e, k) => {
        return Math.min(...arr.slice(s, e+1).filter(value => value > k), Number.MAX_VALUE);
    };
    let answer = [];
    
    for (let i = 0; i < queries.length; i++) {
        let [s, e, k] = queries[i];
        let minVal = checker(arr, s, e, k);
        answer.push(minVal === Number.MAX_VALUE ? -1 : minVal);
    }
    
    return answer;
}