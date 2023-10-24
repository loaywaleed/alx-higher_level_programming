#!/usr/bin/node
// status code of get request

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(fileName, body, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
}
);
