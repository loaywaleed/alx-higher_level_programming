#!/usr/bin/node
/* printing second biggest number */

const args = process.argv;
if (args[2]) {
  let max = args[2];
  let secondMax = 0;
  for (let i = 2; i < args.length; i++) {
    if (args[i] > max) {
      secondMax = max;
      max = args[i];
    }
  }
  console.log(secondMax);
} else {
  console.log(0);
}
