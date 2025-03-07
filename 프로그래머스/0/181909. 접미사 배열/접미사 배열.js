function solution(my_string) {
    var answer = [];
    
    let chars = ''
    for (let char of [...my_string].reverse()) {
        chars = char + chars;
        answer.push(chars);
    }
    return answer.sort();
}