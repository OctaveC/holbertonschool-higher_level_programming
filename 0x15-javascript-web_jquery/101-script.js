$('DIV#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
$('DIV#remove_item').click(function () {
  const list = $('ul.my_list li');
  if (list.length > 0) {
    list[list.length - 1].remove();
  }
});
$('DIV#clear_list').click(function () {
  $('ul.my_list').empty();
});
