#!/usr/bin/node
/**
 * Print all characters of a Star Wars movie, where the episode number matches
 * a given integer, passed as the first argument.
 */
const request = require('request');
const process = require('process');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request({ url: url, json: true }, function (error, response, movie) {
  if (!error && response.statusCode === 200) {
    for (const charUrl of movie.characters) {
      request({ url: charUrl, json: true }, function (err, resp, character) {
        if (!err && resp.statusCode === 200) {
          console.log(character.name);
        }
      });
    }
  }
});
