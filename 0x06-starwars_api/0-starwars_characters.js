#!/usr/bin/node

const request = require('request');

const args = process.argv;
const movieId = args[2];

request({ url: `https://swapi-api.alx-tools.com/api/films/${movieId}`, json: true }, (error, response, body) => {
  if (response.statusCode === 200) {
    const data = body.characters;

    data.forEach(character => {
      request({ url: character, json: true }, (error, response, body) => {
        if (response.statusCode === 200) {
          const name = body.name;
          console.log(name);
        } else {
          console.error(error);
        }
      });
    });
  } else {
    console.error(error);
  }
});
