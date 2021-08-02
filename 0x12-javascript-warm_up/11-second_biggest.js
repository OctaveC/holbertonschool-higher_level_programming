#!/usr/bin/node

const a = parseInt(process.argv[2]);
if (Number.isNaN(a) || process.argv.length <= 3) {
  console.log(0);
} else {
  const b = process.argv.slice(2);
  const c = Math.max(...b);
  const d = b.indexOf(String(c));
  b[d] = -Infinity;
  console.log(Math.max(...b));
}
