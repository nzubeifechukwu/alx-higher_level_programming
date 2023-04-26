#!/usr/bin/node
/**
 * Display the status code of a GET request using the request module, where
 * the URL to request is passed as the first argument
 */
const process = require('process');
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response.statusCode);
});
