let phatbeat = require('../build/phatbeat');
let maxLoops = 5;
let currentLoop = 0;
//must be between 0.1 and 1.0
let brightness = 1.0;
let delay = 100;

phatbeat.init_led();
setLEDColourRecursive(15);

function setLEDColourRecursive(ledInt) {
    phatbeat.changeSingleLED(ledInt, ledInt % 2 === 0 ? 255 : 0, 0, ledInt % 2 > 0 ? 255 : 0, brightness, true);
    setTimeout(function () {
        phatbeat.turnOffAllLEDs(true);
        let newLed;
        if (ledInt === 0 || ledInt === 15) {
            currentLoop++;
        }
        if (currentLoop <= maxLoops) {
            newLed = currentLoop % 2 === 0 ? ++ledInt : --ledInt;

            setLEDColourRecursive(newLed);
        }
        else {
            phatbeat.teardown(false);
        }
    }, delay);
}