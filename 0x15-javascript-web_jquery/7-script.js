$(function () {
  $.get(
    "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    function (response, status) {
      if (status === "success") {
        $("#character").text(response.name);
      }
    }
  );
});
