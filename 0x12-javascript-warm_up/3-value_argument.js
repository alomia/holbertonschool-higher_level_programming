#!/usr/bin/node

const argument = process.argv[2] != null;

if (argument == false) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
