module.exports = function(flotilla, args){
    return {
        input: {
            x: parseInt(args[1]), 
            y: parseInt(args[2]), 
            button: parseInt(args[0])
        }
    }
}
