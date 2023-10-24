#!/usr/bin/node
// Read contents of a file

const fs = require('fs');
const argv = process.argv;
fs.readFile(argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
