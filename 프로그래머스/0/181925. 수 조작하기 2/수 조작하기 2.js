function solution(numLog) {
    return numLog.slice(1).reduce((acc, cur, idx) =>{
        const dif = cur - numLog[idx];
        if (dif === 1) return acc + 'w';
        if (dif === -1) return acc + 's';
        if (dif === 10) return acc + 'd';
        if (dif === -10) return acc + 'a';
        return acc
    }, '');
}
