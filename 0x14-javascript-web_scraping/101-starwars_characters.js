#!/usr/bin/node
// counting number of movies that a character appeared in

const request = require('request');
const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
    if (error) {
        console.log(error);
    }
    const charactersUrl = JSON.parse(body).characters;
    charactersUrl.forEach(charUrl => {
        request(charUrl, (err, res, body2) => {
            if (err) {
                console.log(err);
            }
            const parsedCharacter = JSON.parse(body2).name;
            console.log(parsedCharacter);
        });
    });
}
);
