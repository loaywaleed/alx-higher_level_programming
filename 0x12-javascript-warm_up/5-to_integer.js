#!/usr/bin/node
/* Converting first arg to integer */

if (!(isNaN(process.argv[2]))) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
}
