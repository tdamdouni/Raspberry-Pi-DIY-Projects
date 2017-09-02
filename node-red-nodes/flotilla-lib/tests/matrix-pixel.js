var f = require('../lib');
var c = new f();

var blink = false;

setInterval(function(){

    var matrix = c.modules[0];

    if(matrix && typeof matrix.set_pixel === "function"){
        matrix.set_pixel(0,0,blink);
        matrix.set_pixel(7,7,!blink);
        matrix.show();
        blink = !blink;
    }

},500);
