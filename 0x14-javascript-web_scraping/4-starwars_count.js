#!/usr/bin/node
/**
 * Print the number of movies the character `Wedge Antilles`, with ID 18,
 * starred in. The API url `https://swapi-api.alx-tools.com/api/films/` is
 * passed in as the first argument.
 */
const request = require('request');
const process = require('process');

const url = process.argv[2];

request({ url: url, json: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    let filmCount = 0;
    for (const film of body.results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          filmCount++;
        }
      }
    }
    console.log(filmCount);
  }
});
