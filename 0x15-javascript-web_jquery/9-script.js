$(document).ready(function () {
  // Make an AJAX request to fetch translation data
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (data) {
      const helloTranslation = data.hello;

      $('#hello').text(helloTranslation);
    },
    error: function () {
      $('#hello').text('Error fetching data.');
    },
  });
});
