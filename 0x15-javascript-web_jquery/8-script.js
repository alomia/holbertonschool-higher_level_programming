$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      for (const item of data.results) {
        $('#list_movies').append(`<li>${item.title}</li>`);
      }
    }
  });
});
