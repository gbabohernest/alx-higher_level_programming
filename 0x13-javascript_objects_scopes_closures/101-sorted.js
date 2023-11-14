#!/usr/bin/node

const dictionary = require('./101-data').dict;

const usrIDsByOccurrence = {};

for (const usrID in dictionary) {
  const occurrence = dictionary[usrID];

  if (!usrIDsByOccurrence[occurrence]) {
    // occurrence is not key in dict, init it with an empty array as value
    usrIDsByOccurrence[occurrence] = [];
  }
  // if it does, push the corresponding occurrence in the dict
  usrIDsByOccurrence[occurrence].push(usrID);
}

console.log(usrIDsByOccurrence);
