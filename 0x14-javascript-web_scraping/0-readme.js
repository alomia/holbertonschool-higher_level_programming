#!/usr/bin/node
// Reads the contents of a file
import fs from 'fs';

const file = process.argv[2]

fs = require('fs');
fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
