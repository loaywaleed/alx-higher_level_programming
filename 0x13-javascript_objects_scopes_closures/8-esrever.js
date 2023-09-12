#!/usr/bin/node
/* returning reverse of a list */

exports.esrever = function (list) {
  const newList = [];
  for (let i = (list.length - 1); i >= 0; i--) {
    newList[list.length - i - 1] = list[i];
  }
  return newList;
};
