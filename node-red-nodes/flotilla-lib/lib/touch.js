module.exports = function(flotilla, args){
    return {
        input: {
            button1: args[0] === "1",
            button2: args[1] === "1",
            button3: args[2] === "1",
            button4: args[3] === "1",
        }
    };
}
