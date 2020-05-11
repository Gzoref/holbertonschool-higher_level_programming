#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 &&
        (h = parseInt(h)) > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
