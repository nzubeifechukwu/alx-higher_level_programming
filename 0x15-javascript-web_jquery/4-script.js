$(function () {
  $("#toggle_header").on("click", function () {
    if ($("header").hasClass("green")) {
      $("header").toggleClass("green");
      $("header").toggleClass("red");
    } else {
      $("header").toggleClass("red");
      $("header").toggleClass("green");
    }
  });
});
