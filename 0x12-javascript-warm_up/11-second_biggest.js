#!/usr/bin/node

const argc = process.argv.length - 2;

arrayNumbers = [];

if (argc <= 1) {
  console.log('0');
} else {
  for (let step = 1; step <= argc; step++) {
    arrayNumbers.push(process.argv[step + 1]);
  }

  arrayNumbers.sort();

  console.log(parseInt(arrayNumbers[argc - 1]));
}
