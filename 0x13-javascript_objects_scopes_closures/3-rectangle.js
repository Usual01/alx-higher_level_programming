#!/usr/bin/node
module.exports = class Rectangle {
    // class Rectangle
    constructor (w, h) {
      // initializing the width and height attribute
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      let newString = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
        newString += 'X';
        }
        console.log(newString);
        newString = '';
      }
    }
  };