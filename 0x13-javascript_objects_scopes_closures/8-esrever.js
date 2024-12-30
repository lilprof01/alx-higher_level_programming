#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  let i = list.length;

  while (i > 0) {
    reverseList.push(list[i - 1]);
    i--;
  }
  return reverseList;
};
