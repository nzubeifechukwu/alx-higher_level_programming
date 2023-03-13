#!/usr/bin/node

/*
 * Finds the second biggest integer in a list of arguments
 */
const len = process.argv.length
let args = process.argv

if (len <= 3) {
  console.log(0);
} else {
  args.sort();
  console.log(parseInt(args[len - 2]));
}
