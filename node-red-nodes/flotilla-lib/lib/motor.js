module.exports = function(flotilla, args, channel, module){
    return {
        output: {
            speed: function(value){
                flotilla.updateModule(channel, [value]);
            }
        }
    }
}
