#!/usr/bin/node

const num = process.argv[2];

if (num) {
  for (let col = 0; col < num; col++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
