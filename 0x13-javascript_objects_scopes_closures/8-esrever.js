#!/usr/bin/node

exports.esrever = function (list) {
  const revereList = [];
  let listLength = list.length - 1;

  while (listLength >= 0) {
    revereList.push(list[listLength]);
    listLength--;
  }
  return revereList;
};
