#!/usr/bin/node
// A script that writes a string to a file

const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

if (filePath) {
  fs.writeFile(filePath, fileContent, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
}
