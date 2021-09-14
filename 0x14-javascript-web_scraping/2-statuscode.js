#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, answer) => {
  if (err) throw error;
  console.log('code: ' + answer.statusCode);
});
