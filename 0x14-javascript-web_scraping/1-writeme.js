#!/usr/bin/node
/**
 * Write a string, passed as the second argument, to a file, passed as the
 * first argument. The file content must be written in utf-8. If an error
 * occurred while writing, print the error object.
 */
const fs = require('fs');
const process = require('process');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (error) {
  if (error) {
    console.error(error);
  }
});
