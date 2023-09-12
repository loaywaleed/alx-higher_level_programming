#!/usr/bin/node
/* printing method */

const Square2 = require('./5-square');

/* square class */

module.exports = class Square extends Square2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'x';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
