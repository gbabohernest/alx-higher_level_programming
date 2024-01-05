#!/usr/bin/node
// A script that prints the all characters of a Star War movie, right order

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

    const printCharacter = (index) => {
      if (index < characters.length) {
        request(characters[index], (err, response, body) => {
          if (!err) {
            const characterInMovie = JSON.parse(body);
            console.log(characterInMovie.name);
            printCharacter(index + 1);
          } else {
            console.log(err);
            // printCharacter(index + 1);
          }
        });
      }
    };
    printCharacter(0);
  });
}
