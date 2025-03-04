function solution(num_list) {
    let answer = [...num_list];
    let lastElement = num_list[num_list.length -1];
    let secLastElement = num_list[num_list.length -2];
    
    if (lastElement > secLastElement) {
        let newElement = lastElement - secLastElement;
        answer.push(newElement);
    } else {
        let newElement = lastElement * 2;
        answer.push(newElement);
    }
    
    return answer;
}