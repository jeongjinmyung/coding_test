function solution(intStrs, k, s, l) {
    var answer = [];
    
    for (is of intStrs) {
        let numStrs = is.slice(s, s+l);
        if (+numStrs > k) {
            answer.push(+numStrs)
        }
    }
    return answer;
}