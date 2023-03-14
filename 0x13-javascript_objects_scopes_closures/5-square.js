#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/*
 * Defines a Square class that inherits from a Rectangle class
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
