#!/usr/bin/node
/* converting from base10 to another base */

exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
