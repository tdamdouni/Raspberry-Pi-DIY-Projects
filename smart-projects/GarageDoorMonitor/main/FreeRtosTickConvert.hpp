/*
 * freeRtosTickConvert.hpp
 *
 *  Created on: Jan 8, 2017
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

 */

#ifndef MAIN_FREERTOSTICKCONVERT_HPP_
#define MAIN_FREERTOSTICKCONVERT_HPP_

#include "freertos/FreeRTOSConfig.h"
#include "freertos/FreeRTOS.h"
#include <cstdint>


inline TickType_t milliseconds2ticks ( uint32_t value_ms )
{
   return (TickType_t) (value_ms / portTICK_RATE_MS);
}

/////////////////////////////////////////////////////////////////////////////////////////////
//
//  To learn more about using C++11 User Defined Literals in your
//  firmware and embedded software, see this post:
//     https://covemountainsoftware.com/2016/11/14/favorite-tools-c11-user-defined-literals/
//
/////////////////////////////////////////////////////////////////////////////////////////////

// C++11 User defined literal to convert a value from "milliseconds" to FreeRTOS ticks.
constexpr TickType_t operator"" _milliseconds ( long double value_ms )
{
   return (TickType_t) (value_ms / portTICK_RATE_MS);
}
constexpr TickType_t operator"" _milliseconds ( unsigned long long value_ms )
{
    return (TickType_t) (value_ms / portTICK_RATE_MS);
}
// C++11 User defined literal to convert a value from "seconds" to FreeRTOS ticks.
constexpr TickType_t operator"" _seconds ( long double value_secs )
{
   return (TickType_t) ((value_secs*1000) / portTICK_RATE_MS);
}
constexpr TickType_t operator"" _seconds ( unsigned long long value_secs )
{
    return (TickType_t) ((value_secs*1000) / portTICK_RATE_MS);
}
// C++11 User defined literal to convert a value from "second" to FreeRTOS ticks.
constexpr TickType_t operator"" _second ( long double value_sec )
{
   return (TickType_t) ((value_sec*1000) / portTICK_RATE_MS);
}
constexpr TickType_t operator"" _second ( unsigned long long value_sec )
{
    return (TickType_t) ((value_sec*1000) / portTICK_RATE_MS);
}


#endif /* MAIN_FREERTOSTICKCONVERT_HPP_ */
