#!/usr/bin/node

const request = require('request');
let count = 0;

request.get(process.argv[2], { json: true }, function (err, answer, body) {
  if (err) console.error(err);
  for (const film of body.results) {
    for (const people of film.characters) {
      if (people.indexOf('people/18') >= 0) {
        count++;
      }
    }
  }
  console.log(count);
});
