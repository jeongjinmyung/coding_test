const readline = require('readline');

const rl = readline.createInterface(
    {
        input:process.stdin,
        output:process.stdout,
    }
);

rl.on('line', (input) =>{
    const [N, M] = input.split(' ').map(Number);
    console.log(N + M);
    rl.close();
});