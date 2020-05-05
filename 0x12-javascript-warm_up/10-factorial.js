#!/usr/bin/node

function factorialize (num) {
  if (isNaN(num) || num <= 1) {
    return 1;
  } else {
    return num * factorialize(num - 1);
  }
}

const num = parseInt(process.argv[2]);

console.log(factorialize(num));
