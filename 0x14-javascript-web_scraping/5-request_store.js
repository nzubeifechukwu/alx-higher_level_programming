#!/usr/bin/node
/**
 * Print the number of movies the character `Wedge Antilles`, with ID 18,
 * starred in. The API url `https://swapi-api.alx-tools.com/api/films/` is
 * passed in as the first argument.
 */
const fs = require('fs');
const process = require('process');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request({ url: url, json: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', function (error) {
      if (error) {
        console.error(error);
      }
    });
  }
});
