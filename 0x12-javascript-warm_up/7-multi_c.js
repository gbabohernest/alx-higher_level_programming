#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[0];

if (parseInt(firstArg)) {
  const printTimes = parseInt(firstArg);
  for (let i = 0; i < printTimes; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
