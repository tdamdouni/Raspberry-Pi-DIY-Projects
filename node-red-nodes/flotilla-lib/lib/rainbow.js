var path = require('path');
var colours = require(path.resolve(__dirname, './util-colours.js'));

module.exports = function(flotilla, args, channel, module){
    var buffer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]; // 5xR,G,B

    function update() {
        flotilla.updateModule(channel, buffer);
    }

    function set(value){
        if(typeof value === "object" && value.length == 5){
            for(var x = 0; x < 5; x++){
                set_pixel(x, value[x]);   
            }
            return;
        }

        for(var x = 0; x < 5; x++){
            set_pixel(x, value);
        }
    }

    function set_pixel(x, value){
        if(x < 0 || x > 4) return;

        // Hue from 0.0 to 1.0
        if(typeof value === "number"){
            var h = value;
            var s = 1.0;
            var v = 1.0;
            var r, g, b, i, f, p, q, t;
            i = Math.floor(h * 6);
            f = h * 6 - i;
            p = v * (1 - s);
            q = v * (1 - f * s);
            t = v * (1 - (1 - f) * s);

            switch (i % 6) {
                case 0: r = v, g = t, b = p; break;
                case 1: r = q, g = v, b = p; break;
                case 2: r = p, g = v, b = t; break;
                case 3: r = p, g = q, b = v; break;
                case 4: r = t, g = p, b = v; break;
                case 5: r = v, g = p, b = q; break;
            }

            set_pixel(x, {r: Math.round(r * 255), g: Math.round(g * 255), b: Math.round(b * 255)});
            return;
        }

        // Named colours
        if(typeof value === "string" && typeof colours[value] === "object" ){
            var colour = colours[value];
            set_pixel(x,colour);                      
            return;
        }

        // Object colours with R, G, B
        if(typeof value === "object" && typeof value.r === "number" && typeof value.g === "number" && typeof value.b === "number"){
            x*=3;
            buffer[x] = value.r;
            buffer[x+1] = value.g;
            buffer[x+2] = value.b;
            update();
            return;
        }

        if(typeof value === "object" && value.length == 3 && typeof value[0] === "number" && typeof value[1] === "number" && typeof value[2] === "number"){
            x*=3;
            buffer[x] = value[0];
            buffer[x+1] = value[1];
            buffer[x+2] = value[2];
            update();
            return;
        }
    }

    return {
        output: {
            hue:function(hue){
                if(typeof hue === "number") set(hue);
            },
            colour: set
        }
    };
}
