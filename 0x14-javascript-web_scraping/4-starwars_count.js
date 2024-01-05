#!/usr/bin/node
/* A script that prints the number of movies where the character
** Wedge Antilles is present.
*/

const request = require('request');
const endPoint = process.argv[2];
let result = 0;

request(endPoint, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;

    for (let i = 0; i < data.length; i++) {
      const characters = data[i].characters;

      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          result = result + 1;
          break;
        }
      }
    }
    console.log(result);
  }
});
