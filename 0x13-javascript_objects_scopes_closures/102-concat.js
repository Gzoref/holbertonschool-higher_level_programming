#!/usr/bin/node

const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2]);
const fileB = fs.readFileSync(process.argv[3]);

fs.writeFile(process.argv[4], fileA + fileB, function (err) {
  if (err) throw err;
});
