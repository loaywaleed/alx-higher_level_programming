#!/usr/bin/node
// status code of get request

const request = require('request');
const argv = process.argv;

request(argv[2], (error, respone) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ', respone.statusCode);
  }
});
