#!/usr/bin/node

/*
 * Adds two integers
 */
function add (a, b) {
  return a + b;
}

const sum = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
console.log(sum);
