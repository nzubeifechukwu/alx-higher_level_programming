#!/usr/bin/node

const Sq = require('./5-square');

/**
 * Defines a Square class that inherits from another Square class
 */
class Square extends Sq {
  // prints the square using a given or `X` if not character given
  charPrint (c) {
    if (c) {
      let sq = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          sq = sq + c;
        }
        console.log(sq);
        sq = '';
      }
    } else if (c === undefined) {
      super.print();
    }
  }
}

module.exports = Square;
