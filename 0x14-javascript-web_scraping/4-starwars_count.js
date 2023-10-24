#!/usr/bin/node
// status code of get request

const request = require('request');
const url = process.argv[2];
let count = 0;
const id = 18;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const allFilms = JSON.parse(body);
  for (let i = 0; i < allFilms.results.length; i++) {
    if (allFilms.results[i].characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)) {
      count++;
    }
  }
  console.log(count);
}
);
