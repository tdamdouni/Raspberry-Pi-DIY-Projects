/*
 * PatternGenerator.h
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

#ifndef MAIN_PATTERNGENERATOR_H_
#define MAIN_PATTERNGENERATOR_H_

#include <cstdint>
#include <atomic>
#include <vector>
#include "freertos/FreeRTOS.h"
#include "freertos/timers.h"

namespace CoveMountainSoftware
{

/**
 * The PatternGenerator class internally uses
 * a FreeRTOS timer to drive the pattern
 * generation. Therefore the user of this
 * class has the same constraints as a FreeRTOS timer,
 * and should consider those constraints carefully
 * when developing a PatternNewDataPointHandler callback.
 */
class PatternGenerator
{
   public:
      enum class Pattern
      {
         NONE,
         HANN_WINDOW_PULSE,
         HANN_WINDOW_REPEATING,
         NOISE,
         MORSE_CODE_SOS,
         HALF_SCALED_HANN_WINDOW_PULSE,
         HALF_SCALED_HANN_WINDOW_REPEATING,
         BULK_KNIGHT_RIDER,
         SOLID_FULL_SCALE,
         BULK_SOLID_FIRST_HALF,
         BULK_SOLID_SECOND_HALF,
      };

      /**
       * PatternNewDataPointHandler:
       * @arg points: the newly generated data point or points
       * @arg length: length of "points" array
       * @arg pattern: the current pattern generating this data point
       * @arg isComplete: if the pattern is a pulse, this will be 'true' when
       *                  the pulse is complete and the generator is now generating
       *                  infinite 0.0f points.
       */
      typedef void (*PatternNewDataPointHandler)(float* points, int length, Pattern pattern, bool isComplete);

      PatternGenerator();
      virtual ~PatternGenerator();

      /**
       * Start()
       *   Start/restart a pattern, which will continue forever until Stop() is called.
       *
       * @arg pattern: which pattern to generate
       * @arg patternLength: if applicable, the length of the core repeating pattern
       *                     or pulse before pattern goes to infinite 0.0f.
       *                     if bulk, this is the length of the array generated with
       *                     every update
       * @arg msPerPoint: milliseconds of time per data point generation or bulk array generation
       * @arg handler: callback to receive data
       * @arg bulkUpdateCountBeforeZero: number of times to generate a bulk pattern before going
       *                                 to infinite 0.0f. Set to UINT32_MAX for infinite
       */
      void Start(Pattern pattern, uint16_t patternLength, uint32_t msPerPoint,
            PatternNewDataPointHandler handler, uint32_t bulkUpdateCountBeforeZero = UINT32_MAX);

      /**
       * Change pattern only
       */
      void ChangePattern(Pattern pattern, bool resetCount = false, uint32_t bulkUpdateCountBeforeZero = UINT32_MAX );

      /**
       * Restart any ongoing pattern with existing params.
       */
      void Restart();

      /**
       * Stop all activity and go idle. All previous pattern information is
       * lost and Start() must be called with appropriate parameters
       * to start patterns again.
       */
      void Stop();

      /**
       * GetPattern()
       */
      Pattern GetPattern()
      {
         return mPattern;
      }

   private:
      bool IsBulkPattern();
      void EmitNewDataPoint(float data, bool isComplete);
      float CalculateHannPoint(uint32_t count, uint32_t length);
      float CalculateMorseCodeSosPoint(uint32_t count, uint32_t length);
      void  GenerateKnightRider();

      static void TimerTick(TimerHandle_t timer);
      void Tick();
      void GenerateHannWindowPulse(float scaler, bool isRepeating = false);

      TimerHandle_t mTimer;
      Pattern mPattern;
      uint16_t mPatternLength;
      uint32_t mTimePerPoint_ms;
      std::atomic<uint16_t> mPatternCount { 0 };
      PatternNewDataPointHandler mHandler;
      std::vector<float> mBulk;
      uint32_t mBulkUpdateCountBeforeZero;
      int32_t mPatternArbitraryValue;
      int32_t mPatternArbitraryState;
};

} /* namespace CoveMountainSoftware */

#endif /* MAIN_PATTERNGENERATOR_H_ */
