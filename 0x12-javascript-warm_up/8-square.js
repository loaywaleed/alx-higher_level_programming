#!/usr/bin/node
/* Printing a square */

args = process.argv

if (args[2] && !(isNaN(args[2]))) {
  for (let i = 0; i < args[2]; i++) {
      console.log('X'.repeat(args[2]));
  }
} else {
  console.log('Missing size');
}
