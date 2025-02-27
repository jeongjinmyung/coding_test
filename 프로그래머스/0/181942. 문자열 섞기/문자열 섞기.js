function solution(str1, str2) {
    let answer = '';
    let str_len = str1.length
    for (i = 0; i < str_len; i++) {
        answer += str1[i]
        answer += str2[i]
    }
    
    return answer;
}