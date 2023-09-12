#!/usr/bin/node
/* printing the number of arguments printed and the new argument */

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
