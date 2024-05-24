#!/usr/bin/node
// Import the request module
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the API URL
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the API request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const film = JSON.parse(body);

  // Get the list of characters
  const characters = film.characters;

  // Iterate over each character URL
  characters.forEach(characterUrl => {
    // Make a request to get each character's details
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse the character details
      const character = JSON.parse(body);

      // Print the character's name
      console.log(character.name);
    });
  });
});
