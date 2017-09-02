/*     128
 *     --
 *    |  | 64
 *  2  --
 *  8 |  | 32
 *     --  . 1
 *     16
 */
module.exports = function(flotilla, args, channel, module){
    var numberFont = [
        2, // -
        0, // .
        64+8, // /
        252,//0b11111100, 0
        96, //0b01100000, 1
        218,//0b11011010, 2
        242,//0b11110010, 3
        102,//0b01100110, 4
        182,//0b10110110, 5
        190,//0b10111110, 6
        224,//0b11100000, 7
        254,//0b11111110, 8
        230, //0b11100110 9
        0,   // :
        0,   // ;
        0,   // <
        0,   // =
        0,   // >
        0,   // ?
        0,   // @
        0,   // A
        0,   // B
        16+8+2,       // C
        128+64+32+16+8+4, // D
        128+16+8+4+2,     // E
        128+8+4+2,        // F
    ];

    function stringToDisplay(str) {
        if(typeof str === "number") str = str.toString();

        var realChars = 0;
        var display = [0,0,0,0,0,0,0];

        display[4] = 0; // Clear colon
        display[5] = 0; // Clear apostrophe
        display[6] = 128;

        for(var x = 0; x<str.length; x++){
            var ord = str.charCodeAt(x) - 45;

            if(ord == 13 && realChars == 2){ // Special case for :
                display[4] = 1;
            }
            else if(ord == -13){ // Special case for space
                display[realChars] = 0;
                realChars++;
            }
            else if(ord == -6 && realChars == 3){ // Special case for ' mapped to apostrophe
                display[5] = 1;
            }
            else if(ord == 1 && realChars > 0){ // Special case for .
                display[realChars-1] |= 1;
            }
            else if(ord >= 0 && ord < 45+numberFont.length){
                display[realChars] = numberFont[ord];
                realChars++;
            }

            if(realChars == 4) break;
        }

        return display;
    };

    function update(str) {
        var display = stringToDisplay(str);
        flotilla.updateModule(channel, display);
    }

    return {
        output: {
            time: function(d){
                if(typeof d === "number") {
                    d = new Date(d);
                }
                if(!(d instanceof Date)) {
                    return;
                }
                var dparts = d.toISOString().split(/-|T|:|\./);
                var colon = parseInt(dparts[5]) % 2 ? ":" : ""; // Alternates between 1 and 0
                var dstring = dparts[3] + colon + dparts[4]; // HHMM
                update(dstring);
            },
            temperature: function(temp){
                if(typeof temp !== "number") {
                    return;
                }
                temp = temp.toFixed(1);
                if(temp.length < 3) temp = " " + temp;

                update(temp + "'C");
            },
            number: function(number, decimals, alignRight, padding){
                /* Display a number:
                 * - from 0 to 9999
                 * - from 0 to 999.9
                 * - from 0 to 99.99
                 * - from 0 to 9.999
                 */

                if(typeof number !== "number") {
                    return;
                }

                var max = 9999;

                decimals = decimals || 0;
                if(decimals > 3) decimals = 3;

                padding = padding || " ";
                if([':','.','\''].indexOf(padding) > -1 || padding.length == 0) padding = "";

                if(number < 0) max = 999;

                if(number > max / Math.pow(10,decimals)){
                    number = max / Math.pow(10,decimals);
                }
                number = number.toFixed(decimals);

                if(alignRight){
                    while(number.replace(/\:|\.|\'/,'').length < 4){
                        number = padding + number
                    }
                }

                update(number)
            }
        }
    }
}
