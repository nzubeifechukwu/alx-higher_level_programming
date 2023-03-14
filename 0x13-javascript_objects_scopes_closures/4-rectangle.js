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
    // prints the rectangle using `X` character
    let rect = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rect = rect + 'X';
      }
      console.log(rect);
      rect = '';
    }
  }

  rotate () {
    // exchanges the width and height values
    const breadth = this.width;
    this.width = this.height;
    this.height = breadth;
  }

  double () {
    // double the width and height
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
