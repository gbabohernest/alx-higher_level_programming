$(document).ready(function () {
  // Make an AJAX request to fetch Star Wars movie title

  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      // extract movie titles from response
      const movies = data.results;

      //loop through movies, add titles to UL#list_movies
      const ul = $('#list_movies');
      $.each(movies, function (index, movie) {
        ul.append('<li>' + movie.title + '</li>');
      });
    },
    error: function () {
      $('#list_movies').append('<li>Error, cannot fetch movie data.</li>');
    },
  });
});
