var Gpio = require('onoff').Gpio,
    led1 = new Gpio(23, 'out'),
    led2 = new Gpio(24, 'out'),
    iv,
    count = 0,
    state = 1;

iv = setInterval(function() {
	led1.writeSync(state);
	if (state)
	    state = 0;
	else
	    state = 1;
	led2.writeSync(state);
	count = count + 1;
    }, 500);

setTimeout(function() {
	clearInterval(iv);
	console.log("count " + count);
	led1.writeSync(0);
	led1.unexport();
	led2.writeSync(0);
	led2.unexport();
    }, 5000);
