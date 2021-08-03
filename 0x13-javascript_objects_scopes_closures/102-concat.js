#!/usr/bin/node

const fs = require('fs');
const a = process.argv[2];
const b = process.argv[3];
const c = process.argv[4];
const d = fs.readFileSync(a, 'utf8');
const e = fs.readFileSync(b, 'utf-8');

fs.writeFileSync(c, d + e);
