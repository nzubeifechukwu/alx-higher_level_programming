#!/usr/bin/node

/**
 * Find the frequency of an element in a list
 */
exports.nbOccurences = function (list, searchElement) {
  return list.filter(item => item === searchElement).length;
};
