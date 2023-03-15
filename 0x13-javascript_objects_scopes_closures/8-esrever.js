#!/usr/bin/node

/**
 * Reverse a list without using the reverse function
 */
exports.esrever = function (list) {
  const reversed = [];
  for (const item of list) {
    reversed.unshift(item);
  }
  return reversed;
};
