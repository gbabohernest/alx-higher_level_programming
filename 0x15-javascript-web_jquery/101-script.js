// Add, removes and clear LI elements from a list when user clicks
$(document).ready(function () {
  // Add new item to the list
  $('#add_item').on('click', function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  // Remove the last item from the list
  $('#remove_item').on('click', function () {
    $('ul.my_list li:last').remove();
  });

  // Clear all items from the list
  $('#clear_list').on('click', function () {
    $('ul.my_list').empty();
  });
});
