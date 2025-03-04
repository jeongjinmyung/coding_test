function solution(arr, queries) {
    const changer = (arr, num1, num2) => {
        [arr[num1], arr[num2]] = [arr[num2], arr[num1]];
    }
    
    for (let i = 0; i < queries.length; i++) {
        let [num1, num2] = queries[i];
        changer(arr, num1, num2);
    };
    
    return arr;
}