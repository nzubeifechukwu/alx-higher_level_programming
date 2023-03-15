#!/usr/bin/node

/**
 * Import a dictionary of occurrences by user id and compute a dictionary of
 * user ids by occurrence
 */
const dict = require('./101-data').dict;
const userIds = [];

for (const prop in dict) {
  userIds.push(dict[prop]);
}

const distinct = [...new Set(userIds)]; // keep distinct values
distinct.sort((a, b) => a - b); // ascending sort

const newDict = {};

for (const i of distinct) {
  const occ = [];
  for (const prop in dict) {
    if (i === dict[prop]) {
      occ.push(prop);
    }
  }
  newDict[i] = occ;
}

console.log(newDict);
