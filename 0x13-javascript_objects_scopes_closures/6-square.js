#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let printOut = '';
      for (let j = 0; j < this.width; j++) {
        printOut += c;
      }
      console.log(printOut);
    }
  }
}

module.exports = Square;
