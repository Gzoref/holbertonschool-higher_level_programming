#!/usr/bin/node

const myArg = process.argv[2];

if (myArg) {
  console.log(myArg);
} else {
  console.log('No argument');
}
