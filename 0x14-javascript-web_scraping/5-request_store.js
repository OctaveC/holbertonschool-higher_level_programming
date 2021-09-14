#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, answer, body) {
  if (err) console.log(err);
  fs.writeFile(process.argv[3], body, 'utf8', function (erro, data) {
    if (erro) console.log(erro);
  });
});
