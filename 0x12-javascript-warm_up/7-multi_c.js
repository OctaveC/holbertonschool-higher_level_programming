#!/usr/bin/node

const num = process.argv[2];
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let ite = 0; ite < num; ite++) {
    console.log('C is fun');
  }
}
