#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, answer, body) {
  let count = 0;
  if (err) console.log(err);
  const data = JSON.parse(body);
  for (let ite = 0; data.results[ite] !== undefined; ite++) {
    if (data.results[ite].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
