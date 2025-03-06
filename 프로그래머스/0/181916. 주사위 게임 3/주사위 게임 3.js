function solution(a, b, c, d) {
    const counts = {};
    [a, b, c, d].forEach(num => {
        counts[num] = (counts[num] || 0) + 1;
    })
    
    const keys = Object.keys(counts).map(Number);
    const values = Object.values(counts);
    
    if (keys.length === 1) {
        return 1111 * keys[0];
    } else if (keys.length === 2) {
        if (values.includes(3)) {
            const p = keys[values.indexOf(3)];
            const q = keys[values.indexOf(1)];
            return ((10 * p) + q) ** 2;
        } else {
            const [p, q] = keys;
            return (p + q) * Math.abs(p - q);
        }
    } else if (keys.length === 3) {
        const p = keys[values.indexOf(2)];
        const [q, r] = keys.filter(key => counts[key] === 1);
        return q * r;
    } else {
        return Math.min(...keys);
    }
}