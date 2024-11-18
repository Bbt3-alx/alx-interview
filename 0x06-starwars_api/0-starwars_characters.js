#!/usr/bin/node

const request = require('request-promise-native'); // Use promise-based request

const args = process.argv;
const movieId = args[2];

// if (!movieId) {
//   console.log('Please provide a movie ID as the first argument.');
//   process.exit(1);
// }

(async () => {
  try {
    // Fetch the movie details
    const movieResponse = await request({
      url: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
      json: true
    });

    const characterUrls = movieResponse.characters;

    // Fetch characters in order
    for (const characterUrl of characterUrls) {
      try {
        const characterResponse = await request({
          url: characterUrl,
          json: true
        });
        console.log(characterResponse.name);
      } catch (characterError) {
        console.error(characterError.message);
      }
    }
  } catch (movieError) {
    console.error(movieError.message);
  }
})();
