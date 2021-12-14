#!/usr/bin/node

let argumentOne = 'undefined';
let argumentTwo = 'undefined';

if (process.argv[2] != null) {
  argumentOne = process.argv[2];
}

if (process.argv[3] != null) {
  argumentTwo = process.argv[3];
}

console.log(argumentOne, 'is', argumentTwo);
