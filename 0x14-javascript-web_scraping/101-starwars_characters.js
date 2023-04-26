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
    for (let i = 0; i < movie.characters.length; i++) {
      request({ url: movie.characters[i], json: true }, (err, resp, xter) => {
        if (!err && resp.statusCode === 200) {
          console.log(xter.name);
        }
      });
    }
  }
});
