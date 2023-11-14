#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const val = number + 1;
  theFunction(val);
};
