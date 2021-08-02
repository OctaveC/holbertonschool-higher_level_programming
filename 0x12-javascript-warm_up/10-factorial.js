#!/usr/bin/node

function facto (num) {
  if (!num || num < 2) {
    return 1;
  }
  return num * facto(num - 1);
}
console.log(facto(parseInt(process.argv[2])));
