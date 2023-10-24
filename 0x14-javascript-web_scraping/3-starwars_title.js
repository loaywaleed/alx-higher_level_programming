#!/usr/bin/node
// status code of get request

const request = require('request');
const argv = process.argv;

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, function (body) {
  const titleOfFilm = JSON.parse(body).title;
  console.log(titleOfFilm); // Print the HTML for the Google homepage
});
