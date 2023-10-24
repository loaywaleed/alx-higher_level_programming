#!/usr/bin/node
// status code of get request

const request = require('request');
const url = process.argv[2];
let count = 0;
const id = 18;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const allFilms = JSON.parse(body);
  for (let i = 0; i < allFilms.results.length; i++) {
    for (let j = 0; j < allFilms.results[i].characters.length; j++) {
      if (allFilms.results[i].characters[j].includes(`${id}/`)) {
        count++;
      }
    }
  }
  console.log(count);
}
);
