#!/usr/bin/node

const num = process.argv;

if (num.length <= 3) {
  console.log(0);
} else {
  const args = num.slice(2).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
