function solution(my_strings, parts) {
    var answer = '';
    
    for (let i=0;i<my_strings.length;i++) {
        let string = my_strings[i];
        let [s, e] = parts[i];
        answer += string.slice(s, e+1);
    }
    
    return answer;
}