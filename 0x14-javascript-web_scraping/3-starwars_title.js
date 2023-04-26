#!/usr/bin/node
/**
 * Print the title of a Star Wars movie
 * (API endpoint: https://swapi-api.alx-tools.com/api/films/id), where the
 * episode number mathces a given integer, passed as the first argument.
 */
const request = require('request');
const process = require('process');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request({ url: url, json: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    console.log(body.title);
  }
});
