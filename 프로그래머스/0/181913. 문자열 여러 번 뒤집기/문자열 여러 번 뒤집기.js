function solution(my_string, queries) {
    let result = [...my_string];
    
    for (const [s, e] of queries) {
        const reverse = result.slice(s, e+1).reverse();
        result.splice(s, reverse.length, ...reverse);
    }
    
    return result.join('');
}