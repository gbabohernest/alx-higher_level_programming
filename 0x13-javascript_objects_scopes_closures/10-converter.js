#!/usr/bin/node

exports.converter = function (base) {
  return function (n) {
    return parseInt(n).toString(base);
  };
};
