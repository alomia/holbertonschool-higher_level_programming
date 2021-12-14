#!/usr/bin/node

const number = process.argv[2];

if ((process.argv[2] == null) || (number >= 'a' && number <= 'z')) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(number));
}
