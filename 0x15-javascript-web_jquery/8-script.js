$(function () {
  $.get(
    "https://swapi-api.alx-tools.com/api/films/?format=json",
    function (response, status) {
      if (status === "success") {
        $.each(response.results, function (index, result) {
          $("#list_movies").append("<li>" + result.title + "</li>");
        });
      }
    }
  );
});
