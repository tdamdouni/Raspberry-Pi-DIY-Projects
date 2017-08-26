import phatbeat from './phatbeat'
//all other functionality is dependent entirely on hardware

test('has correct number of buttons defined', () => (
    expect(phatbeat.getButtonPins().length).toBe(6)
));

test('has correct led count defined', () => (
    expect(phatbeat.PIXELCOUNT).toBe(16)
))

test('has correct led count per channel', () => (
    expect(phatbeat.CHANNEL_PIXELS).toBe(8)
))