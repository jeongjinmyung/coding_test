function solution(my_string, is_suffix) {
    let mySuf = [];
    let chars = "";
    for (let string of [...my_string].reverse()) {
        chars = string + chars;
        mySuf.push(chars);
    }
    return mySuf.includes(is_suffix) ? 1 : 0;
}