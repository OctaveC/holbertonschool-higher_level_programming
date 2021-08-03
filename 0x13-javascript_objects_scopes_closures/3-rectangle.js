#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let ite = 0; ite < this.height; ite++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
