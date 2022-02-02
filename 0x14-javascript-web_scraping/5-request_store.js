#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

async function Loripsum () {
  await request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    fs.writeFile(file, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  });
}

Loripsum();
