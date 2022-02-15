$(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      $('#hello').append(data.hello);
    }
  });
});
