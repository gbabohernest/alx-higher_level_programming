#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  while (list.length > 0) {
    const item = list.pop();
    reversedList.push(item);
  }
  return reversedList;
};
