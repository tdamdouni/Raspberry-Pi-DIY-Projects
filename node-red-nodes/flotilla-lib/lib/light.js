module.exports = function(flotilla, args){
    return {
        input: {
            visible: parseInt(args[0]),
            ir: parseInt(args[1]),
            lux: parseInt(args[2])
        }
    }
}
