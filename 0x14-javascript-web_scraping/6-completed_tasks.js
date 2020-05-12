#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const completedTask = {};
  for (const todos of JSON.parse(body)) {
    if (todos.completedTask) {
      if (completedTask[todos.userId]) {
        completedTask[todos.userId]++;
      } else {
        completedTask[todos.userId] = 1;
      }
    }
  }
  console.log(completedTask);
});
