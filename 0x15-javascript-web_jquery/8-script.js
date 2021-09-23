$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (thing) {
  for (let ite = 0; ite <= thing.results.length; i++) {
    $('UL#list_movies').append('<li>' + thing.results[ite].title + '</li>');
  }
});
