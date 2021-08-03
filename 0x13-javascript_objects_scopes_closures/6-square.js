#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let ite = 0; ite < this.width; ite++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
