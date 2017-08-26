/*
 * SimpleGpioMonitor.h
 *
 *  Created on: Mar 14, 2017
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

#ifndef MAIN_SIMPLEGPIOMONITOR_H_
#define MAIN_SIMPLEGPIOMONITOR_H_

#include <cstdint>
#include <array>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include <esp_log.h>
#include <driver/gpio.h>
#include "FreeRtosTickConvert.hpp"

namespace CoveMountainSoftware {

/**
 * The SimpleGpioMonitor class provides a 'simple' polling GPIO monitoring
 * capability with no debouncing or other advanced features. The initial use
 * case is monitoring door switches, which are not expected to change often.
 *
 * An object of this class may be statically allocated, and then later the
 * user must call the Init() method to start its internal thread.
 *
 * Each object will create a separate thread.
 */
template<uint8_t NUM_GPIO_PINS, uint8_t POLL_RATE_ms, const std::array<gpio_num_t, NUM_GPIO_PINS>* GPIOs_TO_READ>
class SimpleGpioMonitor {
   public:

      typedef void (*GpioPinChangedHandler)(gpio_num_t pin, int value);
      typedef void (*AnyGpioPinHighLowHandler)(bool isAnyPinHigh);

      SimpleGpioMonitor();
      virtual ~SimpleGpioMonitor();

      /**
       * Init() - starts the thread which will initialize the designated
       *          GPIO pins as input pins (pull down enabled),
       *          and then begin polling/monitoring of the pins.
       */
      void Init(GpioPinChangedHandler changeHandler, AnyGpioPinHighLowHandler anyPinIsHighHandler);

      /**
       * InvalidateAllPins() - set all internal last pin values to an invalid value
       *                       which will result in a refresh of the pin's states
       *                       and associated calles to the registered GpioPinChangedHandler
       *                       callback.
       */
      void InvalidateAllPins()
      {
         mPinsLastValue.fill(-1);
      }

   private:
      static constexpr const char * tag = "gpioMon";
      static void vStaticTask(void *pvParameters);
      void Task();

      bool                           mIsInit;
      GpioPinChangedHandler 	       mChangeHandler;
      AnyGpioPinHighLowHandler       mAnyPinIsHighHandler;
      std::array<int, NUM_GPIO_PINS> mPinsLastValue;
};

/**
 *
 */
template<uint8_t NUM_GPIO_PINS, uint8_t POLL_RATE_ms, const std::array<gpio_num_t, NUM_GPIO_PINS>* GPIOs_TO_READ>
SimpleGpioMonitor<NUM_GPIO_PINS, POLL_RATE_ms, GPIOs_TO_READ>::SimpleGpioMonitor() :
   mIsInit(false),
   mChangeHandler(nullptr),
   mAnyPinIsHighHandler(nullptr),
   mPinsLastValue()
{
   static_assert(GPIOs_TO_READ != nullptr, "PINS_TO_READ must not be null!");
}

/**
 *
 */
template<uint8_t NUM_GPIO_PINS, uint8_t POLL_RATE_ms, const std::array<gpio_num_t, NUM_GPIO_PINS>* GPIOs_TO_READ>
SimpleGpioMonitor<NUM_GPIO_PINS, POLL_RATE_ms, GPIOs_TO_READ>::~SimpleGpioMonitor()
{
   if (mIsInit)
   {
      //setting this to false will cause the thread
      //to exit its while loop and delete itself.
      mIsInit = false;

      //hack delay to ensure object is valid when
      //it executes next polling cycle.
      vTaskDelay(pdMS_TO_TICKS(POLL_RATE_ms + 10));
   }
}

/**
 *
 */
template<uint8_t NUM_GPIO_PINS, uint8_t POLL_RATE_ms, const std::array<gpio_num_t, NUM_GPIO_PINS>* GPIOs_TO_READ>
void SimpleGpioMonitor<NUM_GPIO_PINS, POLL_RATE_ms, GPIOs_TO_READ>::Init(GpioPinChangedHandler changeHandler,
                                                                         AnyGpioPinHighLowHandler anyPinIsHighHandler)
{
   mChangeHandler = changeHandler;
   mAnyPinIsHighHandler = anyPinIsHighHandler;
   if(mIsInit == false)
   {
      xTaskCreate(&vStaticTask, "gpioMonTask", configMINIMAL_STACK_SIZE, this, configMAX_PRIORITIES - 5, NULL);
   }
}

/**
 * static method to kick off the actual object's Task() method
 */
template<uint8_t NUM_GPIO_PINS, uint8_t POLL_RATE_ms, const std::array<gpio_num_t, NUM_GPIO_PINS>* GPIOs_TO_READ>
void SimpleGpioMonitor<NUM_GPIO_PINS, POLL_RATE_ms, GPIOs_TO_READ>::vStaticTask(void *pvParameters)
{
   auto myself =
         static_cast<SimpleGpioMonitor<NUM_GPIO_PINS, POLL_RATE_ms, GPIOs_TO_READ>*>(pvParameters);
   myself->Task();
}

/**
 * the object's actual Task(). This is where the GPIO pins are
 * monitored in a simple polling loop/task.
 */
template<uint8_t NUM_GPIO_PINS, uint8_t POLL_RATE_ms, const std::array<gpio_num_t, NUM_GPIO_PINS>* GPIOs_TO_READ>
void SimpleGpioMonitor<NUM_GPIO_PINS, POLL_RATE_ms, GPIOs_TO_READ>::Task()
{
   mIsInit = true;

   ESP_LOGI(tag, "started...");

   InvalidateAllPins();

   uint64_t pinsMask = 0;
   for(auto pin : *GPIOs_TO_READ)
   {
      pinsMask |= (1 << pin);
   }

   gpio_config_t io_conf;
   io_conf.intr_type = GPIO_INTR_DISABLE;
   io_conf.pin_bit_mask = pinsMask;
   io_conf.mode = GPIO_MODE_INPUT;
   io_conf.pull_up_en = GPIO_PULLUP_DISABLE;
   io_conf.pull_down_en = GPIO_PULLDOWN_ENABLE;
   gpio_config(&io_conf);

   while(mIsInit)
   {
      vTaskDelay(pdMS_TO_TICKS(POLL_RATE_ms));
      gpio_set_level(GPIO_NUM_5, 1);

      for(int i=0; i < GPIOs_TO_READ->size(); i++)
      {
         auto pin = GPIOs_TO_READ->at(i);
         int pinLevel = gpio_get_level(pin);

         if(pinLevel != mPinsLastValue[i])
         {
            ESP_LOGI("main", "pin %d is now %d...", (int)pin, pinLevel);
            mPinsLastValue[i] = pinLevel;

            if(mChangeHandler)
               mChangeHandler(pin, pinLevel);
         }
      }

      bool isAnySwitchOpen = false;
      for(auto value : mPinsLastValue)
      {
         //"high" pins mean the garage/switch is open. Garage is up/high, so the GPIO is high
         if(value > 0)
         {
            isAnySwitchOpen = true;
            break;
         }
      }

      if(mAnyPinIsHighHandler)
         mAnyPinIsHighHandler(isAnySwitchOpen);
   }

   vTaskDelete(NULL);
}

} /* namespace CoveMountainSoftware */

#endif /* MAIN_SIMPLEGPIOMONITOR_H_ */
