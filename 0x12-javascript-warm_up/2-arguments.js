#!/usr/bin/node

import { argv } from 'process';

const argc = argv.length;

if (argc <= 2) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
