#!/usr/bin/node
// status code of get request

const request = require('request');
const argv = process.argv;

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    const titleOfFilm = JSON.parse(body).title;
    console.log(titleOfFilm);
  }
});
