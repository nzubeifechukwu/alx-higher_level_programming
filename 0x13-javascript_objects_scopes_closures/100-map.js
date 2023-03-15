#!/usr/bin/node

/**
 * Import an array and compute a new array
 */
const list = require('./100-data').list;
const newList = list.map(x => x * list.indexOf(x));
console.log(list);
console.log(newList);
