#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[0];

if (parseInt(firstArg)) {
  const printTimes = parseInt(firstArg);
  for (let i = 0; i < printTimes; i++) {
    let row = '';
    for (let j = 0; j < printTimes; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
