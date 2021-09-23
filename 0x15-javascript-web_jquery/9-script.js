$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (thing) {
  $('DIV#hello').text(thing.hello);
});
