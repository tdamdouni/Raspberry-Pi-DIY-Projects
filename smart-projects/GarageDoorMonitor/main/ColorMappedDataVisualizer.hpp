/*
 * Visualizer.h
 *
 *  Created on: Dec 30, 2016
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

#ifndef _DATA_VISUALIZER_H_
#define _DATA_VISUALIZER_H_

#include <cstdint>
#include <array>
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include "freertos/task.h"
#include <esp_log.h>
#include <driver/gpio.h>
#include <driver/rmt.h>
#include <stdlib.h>
#include "led_strip/led_strip.h"
#include <algorithm>
#include "FreeRtosTickConvert.hpp"

namespace CoveMountainSoftware
{

/**
 * Each ColorMappedDataVisualizer instantiation creates a thread as well.
 * All led strip control occurs in the visualizer's thread context.
 * All memory controlled by this class is statically allocated
 * via the template parameters, especially NUM_PIXELS_
 *
 * The user must call Init() before sending any data points.
 *
 * NOTE: the underlying "led_strip" component being used
 *       is basically an "init only", no delete component,
 *       so recommend only creating, not deleting,
 *       this class.
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
class ColorMappedDataVisualizer
{
   public:
      ColorMappedDataVisualizer();
      virtual ~ColorMappedDataVisualizer();

      /**
       * Initialize the internal thread context
       * and clear the LED strip. Ready for data.
       */
      void Init();

      /**
       * Async give a data point to the object
       * to add to the visualization.
       */
      bool GiveDataPoint(float pt);

      /**
       * Async give a data point to the
       * object, which will be used to fill
       * the entire led light strip
       */
      bool FillAllWithDataPoint(float pt);

      /**
       * Async give data points to the object
       * replacing all points.
       * @arg points: pointer to an array
       *              of floats that is assumed
       *              to be the same length
       *              as NUM_PIXELS_
       *  @arg pointsLen: length of array 'points'.
       *      if len is greater than NUM_PIXELS_, extra
       *      points are dropped
       */
      bool GiveDataPoints(float* points, uint16_t pointsLen);

      /**
       * Change color map to simple red scale,
       * 0.0 == off/black
       * 1.0 == full red.
       */
      bool ChangeColorsToRedScale();

      /**
       * Change color map to standard heat map
       */
      bool ChangeColorsToHeatMap();

   private:

      enum CommandType
      {
         PUSH_PT,
         FILL_ALL,
         PUSH_POINTS,
         RED_COLOR_MAP,
         HEAT_MAP_COLOR_MAP,
      };

      struct Command
      {
         Command() : cmd(PUSH_PT), data(0)  {}
         Command(CommandType c, float pt) : cmd(c), data(pt) {}

         CommandType cmd;
         float       data;
      };

      static constexpr const char * tag = "visualizer";
      static void vStaticTask(void *pvParameters);
      void Task();
      void GetMappedColor(float value, led_color_t& color);
      void ExecPushPt(float pt);
      void ExecFillAll(float pt);
      void ExecPushPoints();
      void ExecSetupRedColorMap();
      void ExecSetupHeatColorMap();
      void UpdateAndFlipBuffers();
      bool SendCmd(CommandType type, float data);

      std::array<led_color_t, NUM_PIXELS_> mDataPoints;
      std::array<struct led_color_t, NUM_PIXELS_> mLedStripBuf1;
      std::array<struct led_color_t, NUM_PIXELS_> mLedStripBuf2;
      struct led_strip_t mLedStrip;
      bool mIsInit;
      QueueHandle_t mQueue;

      static constexpr uint8_t MAX_COLOR_BREAK_POINTS = 7;
      uint8_t mNumColors;
      float mColors[MAX_COLOR_BREAK_POINTS][3] = { { 0, 0, 0 }, //black
                                                   { 0, 0, 1 }, //blue
                                                   { 0, 1, 1 }, //cyan
                                                   { 0, 1, 0 }, //green
                                                   { 1, 1, 0 }, //yellow
                                                   { 1, 0, 0 },  //red
                                                   { 1, 1, 1 }  //white
                                                 };
};

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::ColorMappedDataVisualizer() :
      mDataPoints(),
      mLedStripBuf1(),
      mLedStripBuf2(),
      mLedStrip(),
      mIsInit(false),
      mQueue(0),
      mNumColors(MAX_COLOR_BREAK_POINTS)
{
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
bool ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::ChangeColorsToRedScale()
{
   if (!mIsInit)
   {
      ESP_LOGE(tag, "ChangeColorsToRedScale() called before init!\n");
      return false;
   }

   return SendCmd(RED_COLOR_MAP, 0.0f);
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
bool ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::ChangeColorsToHeatMap()
{
   if (!mIsInit)
   {
      ESP_LOGE(tag, "ChangeColorsToRedScale() called before init!\n");
      return false;
   }

   return SendCmd(HEAT_MAP_COLOR_MAP, 0.0f);
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::~ColorMappedDataVisualizer()
{
   if (mIsInit)
   {
      //setting this to false will cause the thread
      //to exit its while loop and delete itself.
      //however, the led_strip module does not have currently have a delete,
      //so its internal thread context will live on
      mIsInit = false;
      GiveDataPoint(0); //send msg to thread so it can act on mIsInit change.
      vTaskDelay(20_milliseconds);
   }
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::Init()
{
   if(false == mIsInit)
   {
      xTaskCreate(&vStaticTask, "vizTask", configMINIMAL_STACK_SIZE, this, configMAX_PRIORITIES - 1, NULL);
   }
}

/**
 *  GiveDataPoint()
 *  @arg point: float between 0.0 and 1.0. will be clipped automatically if outside
 *              that range.
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
bool ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::GiveDataPoint(float point)
{
   if (!mIsInit)
   {
      ESP_LOGE(tag, "GiveDataPoint() called before init!\n");
      return false;
   }

   //clip to [0.0 .. 1.0]
   point = std::min(point, 1.0f);
   point = std::max(point, 0.0f);

   return SendCmd(PUSH_PT, point);
}

/**
 *  GiveDataPoints()
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
bool ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::GiveDataPoints(float* points, uint16_t pointsLen)
{
   if (!mIsInit)
   {
      ESP_LOGE(tag, "GiveDataPoint() called before init!\n");
      return false;
   }

   //this is not thread safe, but to avoid
   //yet another copy of data, lets copy the pixels now
   //and then send a msg for the final update to the led strip
   for(int i = 0; i < std::min(NUM_PIXELS_,pointsLen); i++)
   {
      led_color_t color;
      GetMappedColor(points[i], color);
      mDataPoints[i] = color;
   }

   return SendCmd(PUSH_POINTS, 0.0f);
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
bool ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::SendCmd(CommandType type,
      float data)
{
   Command cmd(type, data);

   BaseType_t rtn = xQueueSend(mQueue, &cmd, 1_second);
   if (rtn != pdPASS)
   {
      ESP_LOGE(tag, "Queue Send failure!\n");
      return false;
   }

   return true;
}

/**
 *  FillAllWithDataPoint()
 *  @arg point: float between 0.0 and 1.0. will be clipped automatically if outside
 *              that range. Fill fill the entire led strip.
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
bool ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::FillAllWithDataPoint(float point)
{
   if (!mIsInit)
   {
      ESP_LOGE(tag, "GiveDataPoint() called before init!\n");
      return false;
   }

   //clip to [0.0 .. 1.0]
   point = std::min(point, 1.0f);
   point = std::max(point, 0.0f);

   return SendCmd(FILL_ALL, point);
}

/**
 * static method to kick off the actual object's Task() method
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::vStaticTask(void *pvParameters)
{
   auto myself =
         static_cast<ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>*>(pvParameters);
   myself->Task();
}

/**
 * the object's actual Task(). This is where the led strip is initialized
 * and ongoing updates to the visualization take place.
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::Task()
{
   mIsInit = true;

   mQueue = xQueueCreate(3, sizeof(Command));
   if (mQueue == nullptr)
   {
      ESP_LOGE(tag, "Fatal! Queue create failed!\n");
   }

#define LED_STRIP_RMT_INTR_NUM 20U  //doesn't seem to be applicable/needed anymore...

   mDataPoints.fill(led_color_t());
   mLedStripBuf1.fill(led_color_t());
   mLedStripBuf2.fill(led_color_t());
   memset(&mLedStrip, 0, sizeof(led_strip_t));

   ESP_LOGI(tag, "started...");

   mLedStrip.rgb_led_type = RGB_LED_TYPE_WS2812;
   mLedStrip.rmt_channel = RMT_CHANNEL_;
   mLedStrip.rmt_interrupt_num = LED_STRIP_RMT_INTR_NUM;
   mLedStrip.gpio = GPIO_NUM_;
   mLedStrip.led_strip_buf_1 = mLedStripBuf1.data();
   mLedStrip.led_strip_buf_2 = mLedStripBuf2.data();
   ;
   mLedStrip.led_strip_length = NUM_PIXELS_;
   mLedStrip.access_semaphore = xSemaphoreCreateMutex();
   bool led_init_ok = led_strip_init(&mLedStrip);
   if (!led_init_ok)
   {
      ESP_LOGE(tag, "led strip init failed!");
   }

   ESP_LOGI(tag, "led strip Init complete...");

   led_strip_clear(&mLedStrip);

   while (mIsInit)
   {
      Command receivedCommand;
      if (xQueueReceive(mQueue, &(receivedCommand), (TickType_t ) portMAX_DELAY))
      {
         gpio_set_level(GPIO_NUM_5, 1); //crude cpu usage monitor

         switch(receivedCommand.cmd)
         {
            case PUSH_PT:
               ExecPushPt(receivedCommand.data);
               break;

            case FILL_ALL:
               ExecFillAll(receivedCommand.data);
               break;

            case PUSH_POINTS:
               ExecPushPoints();
               break;

            case RED_COLOR_MAP:
               ExecSetupRedColorMap();
               break;

            case HEAT_MAP_COLOR_MAP:
               ExecSetupHeatColorMap();
               break;

            default:
               ESP_LOGE(tag, "queue received unknown command!");
               break;
         }
      }
      else
      {
         ESP_LOGE(tag, "queue receive error?");
      }
   }

   //NOTE: the led_strip component does not have delete/cleanup..
   vSemaphoreDelete(mLedStrip.access_semaphore);
   vTaskDelete(NULL);
}

/**
 *
 */
template <uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::GetMappedColor(float value, led_color_t& color)
{
   //http://www.andrewnoske.com/wiki/Code_-_heatmaps_and_color_gradients

   int idx1;        // |-- Our desired color will be between these two indexes in "color".
   int idx2;        // |
   float fractBetween = 0;  // Fraction between "idx1" and "idx2" where our value is.

	if(value <= 0)      {  idx1 = idx2 = 0;            }    // accounts for an input <=0
	else if(value >= 1)  {  idx1 = idx2 = mNumColors-1; }    // accounts for an input >=0
	else
	{
		value = value * (mNumColors-1);        // Will multiply value by appropriate index max.
		idx1  = floor(value);                  // Our desired color will be after this index.
		idx2  = idx1+1;                        // ... and before this index (inclusive).
		fractBetween = value - float(idx1);    // Distance between the two indexes (0-1).
	}

	color.red = (uint8_t)(((mColors[idx2][0] - mColors[idx1][0])*fractBetween + mColors[idx1][0]) * 255);
	color.green = (uint8_t)(((mColors[idx2][1] - mColors[idx1][1])*fractBetween + mColors[idx1][1]) * 255);
	color.blue  = (uint8_t)(((mColors[idx2][2] - mColors[idx1][2])*fractBetween + mColors[idx1][2]) * 255);
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::ExecPushPt(float pt)
{
   led_color_t newColorPt;
   GetMappedColor(pt, newColorPt);

   std::rotate(mDataPoints.rbegin(), mDataPoints.rbegin() + 1, mDataPoints.rend());
   mDataPoints[0] = newColorPt;
   UpdateAndFlipBuffers();
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::ExecFillAll(float pt)
{
   led_color_t newColorPt;
   GetMappedColor(pt, newColorPt);

   mDataPoints.fill(newColorPt);
   UpdateAndFlipBuffers();
}

/**
 *
 */
template <uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::ExecPushPoints()
{
   //we already updated the array elsewhere...
   UpdateAndFlipBuffers();
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::ExecSetupRedColorMap()
{
   mColors[1][0] = 1;
   mColors[1][1] = 0;
   mColors[1][2] = 0;
   mNumColors = 2;
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::ExecSetupHeatColorMap()
{
   mColors[1][0] = 0;
   mColors[1][1] = 0;
   mColors[1][2] = 1;
   mNumColors = MAX_COLOR_BREAK_POINTS;
}

/**
 *
 */
template<uint16_t NUM_PIXELS_, rmt_channel_t RMT_CHANNEL_, gpio_num_t GPIO_NUM_>
void ColorMappedDataVisualizer<NUM_PIXELS_, RMT_CHANNEL_, GPIO_NUM_>::UpdateAndFlipBuffers()
{
   //update the 'led_strip' buffer
   for (int i = 0; i < NUM_PIXELS_; i++)
   {
      bool rtn = led_strip_set_pixel_color(&mLedStrip, i, &(mDataPoints[i]));
      if (rtn == false)
      {
         ESP_LOGE(tag, "err: led_strip_set_pixel_color");
      }
   }

   //now flip internal buffers and show the update
   if (false == led_strip_show(&mLedStrip))
   {
      ESP_LOGE(tag, "err: led_strip_show");
   }
}

} //namespace

#endif /* _DATA_VISUALIZER_H_ */
