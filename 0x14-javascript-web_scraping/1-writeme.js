#!/usr/bin/node
// write contents to a file

const fs = require('fs');
const argv = process.argv;
fs.writeFile(argv[2], argv[3], 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
