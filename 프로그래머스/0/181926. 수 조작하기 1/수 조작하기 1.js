function solution(n, control) {
    const controlArr = control.split('');
    const counter = (arr, value) => arr.reduce((count, currentValue)=> (currentValue === value ? count + 1 : count), 0);
    
    const wCount = counter(controlArr, 'w');
    const sCount = counter(controlArr, 's');
    const dCount = counter(controlArr, 'd');
    const aCount = counter(controlArr, 'a');
    
    return n + (wCount * 1) - (sCount * 1) + (dCount * 10) - (aCount * 10);
}