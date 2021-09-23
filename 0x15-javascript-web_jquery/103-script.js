const url = 'https://fourtonfish.com/hellosalut/?lang=';
$(this).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    $.getJSON(url + $('INPUT#language_code').val(), function (thing) {
      $('DIV#hello').text(thing.hello);
    });
  });

  $('INPUT#language_code').keyup(function (i) {
    if (i.keyCode === 13) {
      $.getJSON(url + $(this).val(), function (thing) {
        $('DIV#hello').text(thing.hello);
      });
    }
  });
});
