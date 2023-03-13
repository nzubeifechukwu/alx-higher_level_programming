#!/usr/bin/node

/*
 * Finds the second biggest integer in a list of arguments
 */
const len = process.argv.length;
let args = process.argv;

if (len <= 3) {
  console.log(0);
} else {
  args = args.slice(2);
  const newArgs = [];
  for (const n of args) {
    newArgs.push(parseInt(n));
  }
  newArgs.sort(function (a, b) { return a - b; }); // sort int arr in asc order
  console.log(newArgs);
  const distinct = [...new Set(newArgs)]; // keeps only distinct values
  console.log(distinct);
  console.log(distinct[distinct.length - 2]);
}
