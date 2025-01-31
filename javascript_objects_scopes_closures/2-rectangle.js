#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If invalid, do not define any properties (effectively making an empty object)
    }
  }
}

module.exports = Rectangle;
