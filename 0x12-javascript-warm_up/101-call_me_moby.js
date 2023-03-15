#!/usr/bin/node

/**
 * Executes a function a given number of times
 */
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    i++;
    theFunction();
  }
};
