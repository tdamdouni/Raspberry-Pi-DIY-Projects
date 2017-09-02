module.exports = function(flotilla, args){
    var red = parseInt(args[0]);
    var green = parseInt(args[1]);
    var blue = parseInt(args[2]);
    var clear = parseInt(args[3]);
    return {
        input: {
            red: Math.round((red/clear) * 255),
            green: Math.round((green/clear) * 255),
            blue: Math.round((blue/clear) * 255),
            clear: clear
        }
    }
}
