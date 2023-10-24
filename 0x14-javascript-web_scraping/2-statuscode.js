#!/usr/bin/node
// status code of get request

const request = require('request');
const argv = process.argv;

request.get(argv[2]).on('response', (response) => {
  console.log('code:', response.statusCode);
});
