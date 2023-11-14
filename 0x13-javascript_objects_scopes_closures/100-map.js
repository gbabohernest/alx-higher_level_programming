#!/usr/bin/node
const numList = require('./100-data').list;

const newArray = [];
numList.map((item, index) => {
  return newArray.push(item * index);
});

console.log(numList);
console.log(newArray);
