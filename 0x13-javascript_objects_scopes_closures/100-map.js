#!/usr/bin/node

const factor = require('./100-data').list;

let map1 = factor.map((index, list1) => index * list1);
console.log(factor);
console.log(map1);
