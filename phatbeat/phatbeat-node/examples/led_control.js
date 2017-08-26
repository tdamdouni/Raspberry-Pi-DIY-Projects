let app = require('express')();
let phat = require("../build/phatbeat");
let path = require("path");

app.post('/led/', function (req, res) {
    phat.init_led(0.8);
    let responseObject = {
        newState : req.headers.state === "0" ? 1 : 0,
        red : Math.floor(Math.random() * 256),
        green : Math.floor(Math.random() * 256),
        blue : Math.floor(Math.random() * 256)
    };

    if (req.headers.state === "0") {
        phat.changeSingleLED(Number(req.headers.pin), responseObject.red, responseObject.green, responseObject.blue, true);

    } else {
        phat.changeSingleLED(Number(req.headers.pin), 0, 0, 0, true);
    }
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(responseObject));
    res.end();
    phat.teardown(false);
});

app.get("/", function (req, res) {
    res.sendFile(path.join(__dirname + "/led_control_form.html"));
});

app.listen(3000, function () {
    console.log("example server started on port 3000");
});