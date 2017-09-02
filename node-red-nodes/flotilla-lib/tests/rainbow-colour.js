var f = require('../lib');
var c = new f();

colours = ["red", "blue", "green", "red", "blue"];

setInterval(function(){

    var rainbow = c.modules[0];

    if(rainbow && typeof rainbow.colour === "function"){
        colours.push(colours.shift());
        rainbow.colour(colours);
    }

},2000);

setTimeout(function(){
setInterval(function(){

    var rainbow = c.modules[0];

    if(rainbow && typeof rainbow.colour === "function"){
        rainbow.colour(colours[0]);
    }

},2000);
},1000);
