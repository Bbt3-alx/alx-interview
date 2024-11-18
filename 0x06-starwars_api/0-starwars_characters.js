#!/usr/bin/node

const request = require('request');
const { promisify } = require('util');
const requestPromise = promisify(request);

const args = process.argv;
const movieId = args[2];

if (!movieId) {
  console.log('Please provide a movie ID as the first argument.');
  process.exit(1);
}

(async () => {
  try {
    // Fetch the movie details
    const movieResponse = await requestPromise({
      url: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
      json: true
    });

    const characterUrls = movieResponse.body.characters;

    // Fetch characters in order
    for (const characterUrl of characterUrls) {
      try {
        const characterResponse = await requestPromise({
          url: characterUrl,
          json: true
        });
        console.log(characterResponse.body.name);
      } catch (characterError) {
        console.error(`Failed to fetch character: ${characterUrl}`, characterError.message);
      }
    }
  } catch (movieError) {
    console.error('Failed to fetch movie details:', movieError.message);
  }
})();
