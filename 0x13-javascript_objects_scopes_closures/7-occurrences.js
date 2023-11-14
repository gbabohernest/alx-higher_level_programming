#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numOfOccurrences = 0;

  list.forEach((item) => {
    if (item === searchElement) {
      numOfOccurrences++;
    }
  });
  return numOfOccurrences;
};
