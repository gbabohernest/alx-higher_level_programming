$(document).ready(function () {
  $('#add_item').on('click', function () {
    //create a new <li> element
    const newItem = $('<li>').text('Item');

    $('ul.my_list').append(newItem);
  });
});
