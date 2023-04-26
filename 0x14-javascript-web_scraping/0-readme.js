#!/usr/bin/node
/**
 * Read, in utf-8, and print the content of a file,
 * where the first argument is the file path.
 * If an error occurred while reading, print the error object.
 */
const fs = require('fs');
const process = require('process');

fs.readFile(process.argv[2], 'utf-8', function (error, data) {
  if (error) {
    return console.error(error);
  }
  console.log(data.toString());
});
