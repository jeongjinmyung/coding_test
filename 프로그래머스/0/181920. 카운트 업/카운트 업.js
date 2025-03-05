function solution(start_num, end_num) {
    let size = end_num - start_num + 1;
    return Array(size).fill(start_num).map((x, y) => x+y);
}