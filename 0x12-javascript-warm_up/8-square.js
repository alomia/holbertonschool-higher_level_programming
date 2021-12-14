#!/usr/bin/node

const argv = parseInt(process.argv[2]);

if (isNaN(argv)) {
  console.log('Missing size');
} else {
  for (let height = 1; height <= argv; height++) {
    let character = '';
    for (let width = 1; width <= argv; width++) {
      character += 'X';
    }
    console.log(character);
  }
}
