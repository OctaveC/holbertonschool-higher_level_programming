#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let ite = 0; ite < size; ite++) {
    console.log('X'.repeat(size));
  }
}
