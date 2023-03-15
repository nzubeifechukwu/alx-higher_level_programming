#!/usr/bin/node

/**
 * Convert a number from base 10 to another based passed as an argument
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
