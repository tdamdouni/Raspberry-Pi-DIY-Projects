/*
 * PatternGenerator.cpp
 *
 *  Created on: Dec 31, 2016
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

#include "PatternGenerator.h"
#include "freertos/FreeRTOS.h"
#include <esp_log.h>
#include <math.h>
#include <algorithm>
#include "freertos/timers.h"
#include "freertos/semphr.h"
#include "driver/gpio.h"
#include "esp_system.h"
#include "FreeRtosTickConvert.hpp"

namespace CoveMountainSoftware
{

/**
 *
 */
PatternGenerator::PatternGenerator() :
      mTimer(nullptr),
      mPattern(Pattern::NONE),
      mPatternLength(0),
      mTimePerPoint_ms(0),
      mPatternCount(0),
      mHandler(nullptr),
      mBulk(),
      mBulkUpdateCountBeforeZero(0),
      mPatternArbitraryValue(0),
      mPatternArbitraryState(-1)
{

}

/**
 *
 */
PatternGenerator::~PatternGenerator()
{
   if (mTimer != nullptr)
   {
      xTimerDelete(mTimer, 1_second);
   }
}

/**
 *
 */
void PatternGenerator::Start(Pattern pattern, uint16_t patternLength, uint32_t msPerPoint,
      PatternNewDataPointHandler handler, uint32_t bulkUpdateCountBeforeZero)
{
   Stop();

   mPattern = pattern;
   mPatternLength = patternLength;
   mTimePerPoint_ms = msPerPoint;
   mPatternCount = 0;
   mHandler = handler;
   mBulkUpdateCountBeforeZero = bulkUpdateCountBeforeZero;
   mPatternArbitraryValue = 0;
   mPatternArbitraryState = -1;

   if (IsBulkPattern())
   {
      mBulk.resize(mPatternLength);
   }

   mTimer = xTimerCreate("patt", milliseconds2ticks(msPerPoint), pdTRUE, this, TimerTick);
   xTimerStart(mTimer, 1_second);
}

/**
 *
 */
void PatternGenerator::Restart()
{
   mPatternCount = 0;
}

/**
 *
 */
void PatternGenerator::Stop()
{
   if (mTimer != nullptr)
   {
      xTimerDelete(mTimer, 1_second);
      mTimer = nullptr;
   }
   mHandler = nullptr;
   mPattern = Pattern::NONE;
   mPatternLength = 0;
   mTimePerPoint_ms = 0;
   mPatternCount = 0;
   mBulkUpdateCountBeforeZero = 0;
   mPatternArbitraryValue = 0;
   mPatternArbitraryState = -1;
}

/**
 *
 */
void PatternGenerator::ChangePattern(Pattern pattern, bool resetCount, uint32_t bulkUpdateCountBeforeZero)
{
   mPattern = pattern;

   if (resetCount)
   {
      mPatternCount = 0;
   }

   if (IsBulkPattern())
   {
      mBulk.resize(mPatternLength);
      mBulkUpdateCountBeforeZero = bulkUpdateCountBeforeZero;
   }
}

/**
 *
 */
bool PatternGenerator::IsBulkPattern()
{
   switch (mPattern)
   {
      case Pattern::BULK_KNIGHT_RIDER:
      case Pattern::BULK_SOLID_FIRST_HALF:
      case Pattern::BULK_SOLID_SECOND_HALF:
         return true;

      case Pattern::NONE:
      case Pattern::HANN_WINDOW_PULSE:
      case Pattern::HANN_WINDOW_REPEATING:
      case Pattern::NOISE:
      case Pattern::MORSE_CODE_SOS:
      case Pattern::HALF_SCALED_HANN_WINDOW_PULSE:
      case Pattern::HALF_SCALED_HANN_WINDOW_REPEATING:
      case Pattern::SOLID_FULL_SCALE:
         return false;

         //no default on purpose to generate compile error when pattern enum changes.
   }

   return false;
}

/**
 *
 */
void PatternGenerator::GenerateKnightRider()
{
   static constexpr int32_t UNKNOWN = 0;
   static constexpr int32_t FORWARD = 1;
   static constexpr int32_t BACKWARD = 2;

   int32_t& centerOfPulse = mPatternArbitraryValue;
   int32_t& stateOfPulse = mPatternArbitraryState;

   if (mBulkUpdateCountBeforeZero == 0)
   {
      //fill with zeros and emit
      std::fill(mBulk.begin(), mBulk.end(), 0.0f);
      mHandler(mBulk.data(),
               mBulk.size(),
               Pattern::BULK_KNIGHT_RIDER,
               (mBulkUpdateCountBeforeZero == 0));
      return;
   }

   if (mBulkUpdateCountBeforeZero < UINT32_MAX)
   {
      mBulkUpdateCountBeforeZero--;
   }

   if (stateOfPulse <= UNKNOWN)
   {
      stateOfPulse = FORWARD;
      centerOfPulse = mBulk.size() / 2;
   }
   else if (stateOfPulse == FORWARD)
   {
      centerOfPulse += 2;
   }
   else if (stateOfPulse == BACKWARD)
   {
      centerOfPulse -= 2;
   }

   const uint32_t pulseWidth = (uint32_t) ((float) mBulk.size() / 2.5f);

   int start = centerOfPulse - pulseWidth / 2;
   int stop = centerOfPulse + pulseWidth / 2;
   for (int i = 0; i < mBulk.size(); ++i)
   {
      if ((i > start) && (i < stop))
      {
         mBulk[i] = CalculateHannPoint(i - start, pulseWidth);
      }
      else
      {
         mBulk[i] = 0.0f;
      }
   }

   if (mHandler)
   {
      mHandler(mBulk.data(), mBulk.size(), Pattern::BULK_KNIGHT_RIDER,
            (mBulkUpdateCountBeforeZero == 0));
   }

   if (centerOfPulse >= mBulk.size() - 1)
   {
      stateOfPulse = BACKWARD;
   }
   else if (centerOfPulse == 0)
   {
      stateOfPulse = FORWARD;
   }
}

/**
 *
 */
void PatternGenerator::GenerateHannWindowPulse(float scaler, bool repeating)
{
   if (mPatternCount <= mPatternLength)
   {
      EmitNewDataPoint(scaler * CalculateHannPoint(mPatternCount, mPatternLength), false);
      mPatternCount++;
   }
   else
   {
      EmitNewDataPoint(0.0f, true);

      if(repeating)
         mPatternCount = 0;
   }
}

/**
 *
 */
void PatternGenerator::Tick()
{
   if (mHandler == nullptr)
      return;

   //to improve below, perhaps consider
   //static methods and setting a function pointer when
   //pattern is set instead of switch statement

   switch (mPattern)
   {
      case Pattern::NONE:
         EmitNewDataPoint(0.0f, false);
         break;

      case Pattern::HANN_WINDOW_PULSE:
         GenerateHannWindowPulse(1.0);
         break;

      case Pattern::HALF_SCALED_HANN_WINDOW_PULSE:
         GenerateHannWindowPulse(0.5);
         break;

      case Pattern::HANN_WINDOW_REPEATING:
         GenerateHannWindowPulse(1.0, true);
         break;

      case Pattern::HALF_SCALED_HANN_WINDOW_REPEATING:
         GenerateHannWindowPulse(0.5, true);
         break;

      case Pattern::NOISE:
         EmitNewDataPoint((float) esp_random() / (float) UINT32_MAX, false);
         break;

      case Pattern::MORSE_CODE_SOS:
         if (mPatternCount <= mPatternLength)
         {
            EmitNewDataPoint(CalculateMorseCodeSosPoint(mPatternCount, mPatternLength), false);
            mPatternCount++;
         }
         else
         {
            EmitNewDataPoint(0.0f, true);
         }
         break;

      case Pattern::BULK_KNIGHT_RIDER:
         GenerateKnightRider();
         break;

      case Pattern::SOLID_FULL_SCALE:
          EmitNewDataPoint(1.0f, false);
          break;

      case  Pattern::BULK_SOLID_FIRST_HALF:
    	  std::fill(mBulk.begin(), mBulk.end(), 0.0f);
    	  std::fill(mBulk.data(), mBulk.data()+mBulk.size()/2, 1.0f);
    	  mHandler(mBulk.data(),  mBulk.size(),
    			  Pattern::BULK_SOLID_FIRST_HALF, false);
    	  break;

      case Pattern::BULK_SOLID_SECOND_HALF:
    	  std::fill(mBulk.begin(), mBulk.end(), 0.0f);
    	  std::fill(mBulk.data()+mBulk.size()/2, mBulk.data()+mBulk.size(), 1.0f);
    	  mHandler(mBulk.data(),  mBulk.size(),
    			  Pattern::BULK_SOLID_SECOND_HALF, false);
    	  break;

         //no default on purpose to generate compile error when pattern enum changes.
   }
}

/**
 *
 */
void PatternGenerator::EmitNewDataPoint(float data, bool isComplete)
{
   if (mHandler)
   {
      mHandler(&data, 1, mPattern, isComplete);
   }
}

/**
 *
 */
float PatternGenerator::CalculateHannPoint(uint32_t count, uint32_t length)
{
   return 0.5 * (1 - cos(2 * 3.14159265358979323846 * count / length));
}

/**
 *
 */
float PatternGenerator::CalculateMorseCodeSosPoint(uint32_t count, uint32_t length)
{
   float singleDotDashLength = (float) length / 9.1;

   uint32_t dotDashIndex = count / (uint32_t) (singleDotDashLength + 0.5);

   float percentWithinDotDash = (float) (count % (uint32_t) (singleDotDashLength + 0.5))
         / (float) singleDotDashLength;

   switch (dotDashIndex)
   {
      case 0:
      case 1:
      case 2:
      case 6:
      case 7:
      case 8:
         //dot
         if ((percentWithinDotDash < 0.4) || (percentWithinDotDash > 0.6))
            return 0.0;
         else
            return 1.0;
         break;
      case 3:
      case 4:
      case 5:
         //dash
         if ((percentWithinDotDash < 0.2) || (percentWithinDotDash > 0.8))
            return 0.0;
         else
            return 1.0;
         break;
      default:
         return 0.0;
         break;
   }

   return 0.0;
}

/**
 *
 */
void PatternGenerator::TimerTick(TimerHandle_t timer)
{
   gpio_set_level(GPIO_NUM_5, 1); //crude cpu usage monitor
   auto myself = static_cast<PatternGenerator*>(pvTimerGetTimerID(timer));
   myself->Tick();
}

} /* namespace CoveMountainSoftware */

