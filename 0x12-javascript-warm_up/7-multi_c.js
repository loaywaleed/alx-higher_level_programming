#!/usr/bin/node
/* printing c is fun x times */

const args = process.argv;

if (args[2]) {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
