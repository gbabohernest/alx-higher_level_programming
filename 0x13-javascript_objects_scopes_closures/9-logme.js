#!/usr/bin/node

let timesPrinted = 0;
exports.logMe = function (item) {
  console.log(`${timesPrinted}: ${item}`);
  timesPrinted++;
};
