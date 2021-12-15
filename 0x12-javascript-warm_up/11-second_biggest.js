#!/usr/bin/node

const argc = process.argv.length - 2;

const arrayNumbers = [];

if (argc <= 2) {
  console.log('0');
} else {
  for (let step = 1; step <= argc; step++) {
    arrayNumbers.push(process.argv[step + 1]);
  }

  arrayNumbers.sort();

  console.log(arrayNumbers[argc - 1]);
}
