$('INPUT#btn_translate').on('click', function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), function (data) {
    $('DIV#hello').text(data.hello);
  });
});
