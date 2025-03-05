function solution(arr, queries) {
    var answer = [...arr];
    
    for (i=0; i<queries.length; i++) {
        let [s, e, k] = queries[i];
        for (j=s; j<e+1; j++) {
            if (j % k ===0) {
                answer[j] += 1;
            }
        }
    }
    return answer;
}