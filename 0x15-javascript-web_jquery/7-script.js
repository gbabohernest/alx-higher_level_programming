$(document).ready(function () {
  // Make an AJAX request to fetch Star wars character
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function (data) {
      const characterName = data.name;

      // Display the character name in DIV#character
      $('#character').text(characterName);
    },
    error: function () {
      $('#character').text("Opps!!, sorry can't get data");
    },
  });
});
