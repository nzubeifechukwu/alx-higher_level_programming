#!/usr/bin/node

/*
 * Defines a Rectangle class
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rect = rect + 'X';
      }
      console.log(rect);
      rect = '';
    }
  }
}

module.exports = Rectangle;
