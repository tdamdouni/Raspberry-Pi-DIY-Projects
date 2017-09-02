module.exports = function(flotilla, args){
    return {
        input: {
            accelerometer: {
                x: parseInt(args[0]),
                y: parseInt(args[1]),
                z: parseInt(args[2]),
            },
            magnetometer: {
                x: parseInt(args[3]),
                y: parseInt(args[4]),
                z: parseInt(args[5]),
            }
        }
    }
}
