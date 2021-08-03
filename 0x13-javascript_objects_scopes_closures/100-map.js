#!/usr/bin/node

const list = require('./100-data').list;
const map = list.map((x, y) => x * y);

console.log(list);
console.log(map);
