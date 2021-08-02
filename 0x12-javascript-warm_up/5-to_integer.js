#!/usr/bin/node
const variable = process.argv[2];
if (isNaN(variable)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(variable));
}
