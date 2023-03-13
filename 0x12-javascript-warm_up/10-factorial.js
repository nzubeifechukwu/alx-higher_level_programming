#!/usr/bin/node

/*
 * Computes a factorial
 */
const factorial = (num) => {
  if (num === 0 || String(num) === 'NaN') {
    return 1;
  }
  return num * factorial(num - 1);
};

console.log(factorial(parseInt(process.argv[2])));
