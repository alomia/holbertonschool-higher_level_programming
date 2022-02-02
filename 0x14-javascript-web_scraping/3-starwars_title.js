#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];

async function movieTitle () {
  const url = 'https://swapi-api.hbtn.io/api/films/';
  await request(url + episode, function (err, request, body) {
    if (err) {
      console.log(err);
    }
    const obj = JSON.parse(body);
    console.log(obj.title);
  });
}

movieTitle();
