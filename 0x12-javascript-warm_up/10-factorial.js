#!/usr/bin/node

const number = parseInt(process.argv[2]);

let factorial = 1;

for (let step = 1; step <= number; step++) {
  factorial *= step;
}

console.log(factorial)
