var SEC_TO_MS = 1000;
var MAX_INTERVAL_MS = 100;
var last = +new Date();

function move_robot(direction){
  if(!direction){
    return null;
  }
  const now = +new Date();
  if (now - last < MAX_INTERVAL_MS) {
    return;
  }
  last = now;
  $.ajax({
    type: "POST",
    url: "/move_robot",
    data: {
      direction: direction
    },
    timeout: 300,
    success: function(result) {
      console.log(result);
    },
    error: function(result) {
      console.log(result);
    }
  });
}

$(document).keypress(function(e) {
  key = String.fromCharCode(e.charCode).toLowerCase();
  switch(key){
  case 'w':
    move_robot("forward");
    break;
  case 'd':
    move_robot("right");
    break;
  case 's':
    move_robot("back");
    break;
  case 'a':
    move_robot("left");
    break;
  }
});
var tId = null;

function repeat(direction, times){
  move_robot(direction);
  times--;
  if(times<=0){
    tId = null;
    return;
  }
  tId = setTimeout(function() {repeat(direction, times);}, MAX_INTERVAL_MS);
}

$(document).ready(function() {
  $('button').on('click', function() {
      if(tId == null){
        var direction = $(this).val();
        repeat(direction, direction=="forward"? 20:10);
      }
  })
});
