setInterval(function() {

  // Update temperature
  $.get("/temperature", function(data) {
    $("#temperature").html(data.temperature);
  });

  // Update humidity
  $.get("/humidity", function(data) {
    $("#humidity").html(data.humidity);
  });
  
}, 2000);

setInterval(function() {

  // Take picture
  $.get("/camera/snapshot");

  
}, 10000);

setInterval(function() {

  // Reload picture
  d = new Date();
  $("#camera").attr("src","pictures/image.jpg?" + d.getTime());
  
}, 1000);