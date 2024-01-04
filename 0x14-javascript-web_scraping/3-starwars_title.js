#!/usr/bin/node
/* A script that prints the title of a Star War movie
 ** where the episode number matches a given integer.
 */

const request = require('request');
const movieID = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(endPoint, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
