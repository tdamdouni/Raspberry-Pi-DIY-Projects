let phat = require("../build/phatbeat");
let buttons = phat.getButtonPins();

for(let i = 0; i < buttons.length; i++){
    let stream = phat.buttonStream(buttons[i].pin);
    stream.on("pinChange", function(pin, pinState){
        console.log("Pin " + pin + " is now " + (pinState === 1 ? "pressed" : "released"));
    });

    stream.on("monitoring", function(pin){
        console.log("Pin " + pin + " is now being monitored for status changes. Press and hold button for at least 5 seconds to stop monitoring.");
    });

    stream.on("end", function(pin){
        console.log("Pin " + pin + " stream closed.");
    });
}