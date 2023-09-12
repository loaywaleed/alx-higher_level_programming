#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/* Square class */

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
