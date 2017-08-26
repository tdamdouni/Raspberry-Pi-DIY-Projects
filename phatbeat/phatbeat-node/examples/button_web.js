let app = require('express')();
let phat = require("../build/phatbeat");
let path = require("path");
//fastforward
let stream = phat.buttonStream(29);


app.get("/", function (req, res) {
    res.setHeader('Content-Type', 'text/html');
    res.write("button status changes:<br/>")
    stream.on("pinChange", function(pin, pinState){
        res.write("Pin " + pin + " is now " + (pinState === 1 ? "pressed" : "released") + " at " + new Date().toLocaleTimeString() + "<br/>");
    });
    
});

app.listen(3000, function () {
    console.log("example server started on port 3000");
});