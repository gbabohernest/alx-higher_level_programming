#!/usr/bin/node
// A script that gets the content of a web page and stores it in a file.

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const filePath = process.argv[3];

if (URL && filePath) {
  request(URL, (err, response, body) => {
    if (err) {
      console.log(err);
    }

    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
}
