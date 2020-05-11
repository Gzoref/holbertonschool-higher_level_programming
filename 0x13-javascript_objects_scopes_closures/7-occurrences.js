#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let index = 0; index < list.length; index++) {
    if (searchElement === list[index]) {
      count++;
    }
  }
  return count;
};
