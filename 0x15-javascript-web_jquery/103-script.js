// A script that fetches and prints how to say “Hello” depending on the language
 $(document).ready(function() {
      // Function to fetch translation
      function fetchTranslation() {
        const languageCode = $("#language_code").val();

        // Make an AJAX request to fetch the translation
        $.ajax({
          url: 'https://www.fourtonfish.com/hellosalut/hello/',
          method: 'GET',
          data: { lang: languageCode },
          success: function(data) {
            // Display the translation in DIV#hello
            $("#hello").text(data.hello);
          },
          error: function() {
            $("#hello").text('Error fetching translation.');
          }
        });
      }

      // Bind click event to the button
      $("#btn_translate").on("click", fetchTranslation);

      // Bind keypress event to the input field
      $("#language_code").on("keypress", function(event) {
        if (event.which === 13) {
          // 13 is the key code for Enter
          fetchTranslation();
        }
      });
    });
