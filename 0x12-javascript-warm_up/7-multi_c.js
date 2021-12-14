#!/usr/bin/node

const argv = parseInt(process.argv[2]);

if (isNaN(argv)) {
  console.log('Missing number of occurrences');
} else {
  for (let step = 1; step <= argv; step++) {
    console.log('C is fun');
  }
}
