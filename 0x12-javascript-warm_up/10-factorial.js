#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[0];

const factorialRecursive = (num) => {
  if (isNaN(num)) {
    return 1;
  }
  if (num === 0) {
    return 1;
  }

  return num * factorialRecursive(num - 1);
};

console.log(factorialRecursive(firstArg));
