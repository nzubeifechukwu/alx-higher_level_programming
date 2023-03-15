#!/usr/bin/node

/**
 * Import an array and compute a new array
 */
const list = require('./100-data').list;
let i = 0;
const newList = list.map(function (x) { x = x * i; i++; return x; });
console.log(list);
console.log(newList);
