$(document).ready(function () {
  const images = $(".thumbnail")
    .map(function () {
    return $(this).attr("src");
    })
    .get();

  let currentIndex = 0;

  $(".thumbnail").click(function () {
    const clickedSrc = $(this).attr("src");
    currentIndex = images.indexOf(clickedSrc);
    $("#modal-img").attr("src", clickedSrc);
    $("#modal").fadeIn();
  });

  $(".close, #modal").click(function (e) {
    if ($(e.target).is("#modal") || $(e.target).is(".close")) {
      $("#modal").fadeOut();
    }
  });

  $(".next").click(function () {
    currentIndex = (currentIndex + 1) % images.length;
    $("#modal-img").fadeOut(200, function () {
      $(this).attr("src", images[currentIndex]).fadeIn(200);
    });
  });

  $(".prev").click(function () {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    $("#modal-img").fadeOut(200, function () {
      $(this).attr("src", images[currentIndex]).fadeIn(200);
    });
  });
});
