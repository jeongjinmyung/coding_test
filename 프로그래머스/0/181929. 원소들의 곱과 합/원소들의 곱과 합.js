function solution(num_list) {
    const allSum = num_list.reduce((acc, cur)=> acc + cur) ** 2;
    const allMul = num_list.reduce((acc, cur)=> acc * cur);
    
    if (allMul > allSum) {
        return 0;
    } else {
        return 1;
    }
}