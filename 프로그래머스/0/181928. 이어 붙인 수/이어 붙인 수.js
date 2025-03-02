function solution(num_list) {
    let oddStr = "";
    let evenStr = "";
    
    num_list.forEach(num=>{
        if (num % 2 === 0) {
            evenStr += num;
        } else {
            oddStr += num;
        }
    })
    
    return Number(oddStr) + Number(evenStr);
}