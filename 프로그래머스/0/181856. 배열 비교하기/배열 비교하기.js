function solution(arr1, arr2) {
    var answer = 0;
    arr1_len = arr1.length
    arr2_len = arr2.length
    
    if (arr1_len == arr2_len) {
        arr1_sum = arr1.reduce((a, b)=> a+b, 0);
        arr2_sum = arr2.reduce((a, b)=> a+b, 0);
        if (arr1_sum > arr2_sum) {
            answer = 1;
        } else if (arr1_sum < arr2_sum) {
            answer = -1;
        } else {
            answer = 0;
        }
    } else {
        if (arr1_len > arr2_len) {
            answer = 1;
        } else {
            answer = -1;
        }
    }
    return answer;
}