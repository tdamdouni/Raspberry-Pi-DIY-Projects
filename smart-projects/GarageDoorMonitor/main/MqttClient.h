/*
 * MqttClient.h
 *
 *  Created on: Jan 1, 2017
 *      Author: eshlemanm
 *

Copyright (c) <2017> <Matthew Eshleman - https://covemountainsoftware.com/>

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 *
 */

#ifndef MAIN_MQTTCLIENT_H_
#define MAIN_MQTTCLIENT_H_

#include <cstdint>

namespace CoveMountainSoftware
{

namespace MqttClient
{

typedef void (*PatternEventHandler)(int pattern);
typedef void (*SimpleEventHandler)();

/**
 * Start the internal client. Call this after wifi has acquired a valid IP address.
 */
void Start();

/**
 * Stop the internal client. Call this when wifi loses a connection.
 */
void Stop();

/**
 * Register callback for pattern change request.
 */
void RegisterPatternEventHandler(PatternEventHandler handler);

/**
 * Register callback for Mqtt Up and Connected
 */
void RegisterMqttUpEventHandler(SimpleEventHandler handler);

/**
 *  Publish a switch event
 */
void PublishSwitchEvent(uint16_t switchId, uint8_t value);

}

} /* namespace CoveMountainSoftware */

#endif /* MAIN_MQTTCLIENT_H_ */
