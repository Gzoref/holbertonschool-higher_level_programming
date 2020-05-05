#!/usr/bin/node

const myArg = parseInt(process.argv[2]);

if (myArg) {
  console.log(`My number: ${myArg}`);
} else {
  console.log('Not a number');
}
