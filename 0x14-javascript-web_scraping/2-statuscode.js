#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, answer) => {
  if (err) console.log(err);
  console.log('code: ' + answer.statusCode);
});
