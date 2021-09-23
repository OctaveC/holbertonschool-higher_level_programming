$(this).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), function (thing) {
      $('DIV#hello').text(thing.hello);
    });
  });
});
