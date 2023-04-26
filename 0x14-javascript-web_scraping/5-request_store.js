#!/usr/bin/node
/**
 * Get the content of a webpage and store it in a file. The webpage url is
 * passed as the first argument and the file path as the second.
 */
const fs = require('fs');
const process = require('process');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (!error) {
    fs.writeFile(filePath, body, 'utf-8', function (error) {
      if (error) {
        console.error(error);
      }
    });
  }
});
