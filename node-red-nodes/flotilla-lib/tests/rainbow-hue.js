var f = require('../lib');
var c = new f();

var hue = 0;

setInterval(function(){

    hue++;
    hue%=360;

    var rainbow = c.modules[0];

    if(rainbow && typeof rainbow.hue === "function"){
        rainbow.hue(hue/360);
    }

},100);
