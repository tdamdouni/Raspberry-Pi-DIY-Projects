module.exports = function(flotilla, args){
    var temperature = parseInt(args[0]) / 100;
    var pressure = parseInt(args[1]) / 1000;
    return {
        input: {
            temperature: temperature,
            pressure: pressure
        }
    }
}
