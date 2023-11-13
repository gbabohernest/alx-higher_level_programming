#!/usr/bin/node

const factorialRecursive = (num) => {
  if (isNaN(parseInt(num))) {
    return 1;
  }
  if (parseInt(num) === 0) {
    return 1;
  }

  return parseInt(num) * factorialRecursive(num - 1);
};

const arg = process.argv[2];
console.log(factorialRecursive(arg));
