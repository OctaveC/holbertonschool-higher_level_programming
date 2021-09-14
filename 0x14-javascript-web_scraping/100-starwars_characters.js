#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, answer, body) {
  if (err) console.log(err);
  for (const character of JSON.parse(body).characters) {
    request(character, function (erro, answero, body) {
      if (erro) console.log(erro);
      console.log(JSON.parse(body).name);
    });
  }
});
