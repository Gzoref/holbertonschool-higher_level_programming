#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 &&
            (h = parseInt(h)) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rotatedValues = this.width;
    this.width = this.height;
    this.height = rotatedValues;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
