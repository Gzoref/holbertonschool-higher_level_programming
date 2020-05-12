#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  let count = 0;
  for (const result of JSON.parse(body).results) {
    if (result.characters.includes(characterId)) {
      count++;
    }
  }
  console.log(count);
});
