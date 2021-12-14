#!/usr/bin/node

const args = process.argv;

const x = parseInt(args[2]);

try {
  const res = factorial(x);
  console.log(res);
} catch (error) {
  console.log(1);
}

function factorial (x) {
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
