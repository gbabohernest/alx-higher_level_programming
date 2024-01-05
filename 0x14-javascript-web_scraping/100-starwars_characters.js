#!/usr/bin/node
// A script that prints the all characters of a Star War movie

const request = require('request');
const movieID = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

if (movieID) {
  request(endPoint, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach((character) => {
      request(character, (err, response, body) => {
        if (!err) {
          const characterInMovie = JSON.parse(body);
          console.log(characterInMovie.name);
        } else {
          console.log(err);
        }
      });
    });
  });
}
