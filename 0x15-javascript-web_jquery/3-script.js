$(document).ready(function () {
  //Bind click event to DIV#red_header
  $('#red_header').on('click', function () {
    //Add the class 'red' to the <header> element
    $('header').addClass('red');
  });
});
