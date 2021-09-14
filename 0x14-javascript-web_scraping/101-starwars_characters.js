#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const one = function () {
  request(url, function (err, answer, body) {
    if (err) console.log(err);
    second(JSON.parse(body).characters, 0);
  });
};

const two = function (characters, ite) {
  if (characters.length === ite) {
    return;
  }
  request(characters[i], function (erro, answero, body) {
    if (erro) console.log(erro);
    console.log(JSON.parse(body).name);
    two(characters, ++ite);
  });
};

one();
