#!/usr/bin/node
// A script that reads and prints the content of a file

const fs = require('fs');
const filePath = process.argv[2];

if (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
