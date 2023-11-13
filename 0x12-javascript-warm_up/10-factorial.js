#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = parseInt(args[0]);

function factorialRecursive (num) {
  if (isNaN(num) || num < 1) {
    return 1;
  }

  return (num * factorialRecursive(num - 1));
}

console.log(factorialRecursive(firstArg));
