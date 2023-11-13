#!/usr/bin/node

const args = process.argv.slice(2);
const numOfArgs = args.length;

if (numOfArgs < 0 || numOfArgs === 0) {
  console.log('No argument');
} else if (numOfArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
