'use strict';

var _phatbeat = require('./phatbeat');

var _phatbeat2 = _interopRequireDefault(_phatbeat);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

//all other functionality is dependent entirely on hardware

test('has correct number of buttons defined', function () {
    return expect(_phatbeat2.default.getButtonPins().length).toBe(6);
});

test('has correct led count defined', function () {
    return expect(_phatbeat2.default.PIXELCOUNT).toBe(16);
});

test('has correct led count per channel', function () {
    return expect(_phatbeat2.default.CHANNEL_PIXELS).toBe(8);
});