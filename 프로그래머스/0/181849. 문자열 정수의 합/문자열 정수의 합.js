function solution(num_str) {
    var answer = 0;
    
    for(let nums of num_str){
        answer += parseInt(nums);
    }
    return answer;
}