#!/usr/bin/node
// Getting title of a starwars movie

const request = require('request');
const argv = process.argv;

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, function (error, response, body) {
    if (error) {
        console.log(error);
    }
    const titleOfFilm = JSON.parse(body).title;
    console.log(titleOfFilm);
});
