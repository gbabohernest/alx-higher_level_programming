// A script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const languageCode = $('#language_code').val();

    // Make an AJAX request to fetch the translation
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      method: 'GET',
      data: { lang: languageCode },
      success: function (data) {
        // Display the translation in DIV#hello
        $('#hello').text(data.hello);
      },
      error: function () {
        $('#hello').text('Error fetching translation.');
      },
    });
  });
});
