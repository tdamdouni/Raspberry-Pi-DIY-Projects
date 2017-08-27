/**
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

#include "SimpleGpioMonitor.h"
#include "freertos/FreeRTOS.h"
#include "esp_wifi.h"
#include "esp_system.h"
#include "esp_event.h"
#include "esp_event_loop.h"
#include "nvs_flash.h"
#include "driver/gpio.h"
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include "freertos/semphr.h"
#include "freertos/task.h"
#include <esp_log.h>
#include "led_strip/led_strip.h"
#include <math.h>
#include <algorithm>
#include "freertos/timers.h"
#include <math.h>
#include <atomic>
#include "esp_freertos_hooks.h"
#include "ColorMappedDataVisualizer.hpp"
#include "PatternGenerator.h"
#include "MqttClient.h"
#include "wifi_init.h"
#include <esp_log.h>
#include "sdkconfig.h"

using namespace CoveMountainSoftware;

//led strip data visualizer using a heat map style color scheme...
static ColorMappedDataVisualizer<60, RMT_CHANNEL_0, GPIO_NUM_21> m_visualizer;

//our pattern generator for feeding the visualizer
static PatternGenerator m_PatternGenerator;

//switch pins and pin monitor
static constexpr gpio_num_t SWITCH_0_PIN = GPIO_NUM_17;
static constexpr gpio_num_t SWITCH_1_PIN = GPIO_NUM_16;
static const std::array<gpio_num_t, 2> m_PinsToRead { SWITCH_0_PIN, SWITCH_1_PIN };
static SimpleGpioMonitor<2, 250, &m_PinsToRead> m_GpioMonitor;

/**
 *
 */
static esp_err_t wifi_tcp_event_handler(void *ctx, system_event_t *event)
{
   gpio_set_level(GPIO_NUM_5, 1); //crude CPU measurement monitor

   ESP_LOGI("main", "wifi_tcp_event_handler: 0x%x", event->event_id);

   switch (event->event_id)
   {
      case SYSTEM_EVENT_STA_START:
         esp_wifi_connect();
         break;

      case SYSTEM_EVENT_STA_GOT_IP:
         MqttClient::Start();
         break;

      case SYSTEM_EVENT_STA_DISCONNECTED:
         MqttClient::Stop();

         /* This is a workaround as ESP32 WiFi libs don't currently auto reassociate. */
         esp_wifi_connect();
         break;

      default:
         break;
   }
   return ESP_OK;
}

/**
 * PatternGenCallback()
 *   The callback from the pattern generator is used to simply
 *   feed data to our LED strip visualizer.
 */
void PatternGenCallback(float* points, int lenOfPoints, PatternGenerator::Pattern pattern, bool )
{
   gpio_set_level(GPIO_NUM_5, 1); //crude cpu usage monitor

   if(points == nullptr)
      return;

   if(lenOfPoints == 1)
   {
      m_visualizer.GiveDataPoint(*points);
   }
   else
   {
      m_visualizer.GiveDataPoints(points, (uint16_t)lenOfPoints);
   }
}

/**
 *   used as crude cpu meter for
 *   tasks we control.
 *   Turns LED on GPIO 5 off when FreeRTOS is IDLE.
 */
static bool IdleHook()
{
   gpio_set_level(GPIO_NUM_5, 0);
   return true;
}

/**
 * MqttPatternChangeEventHandler()
 *   The callback handler for when the MQTT network announces a new
 *   LED pattern. Basically translates the int to the PatternGenerator class
 *   to setup the new pattern. If the 'int' value does not match, simply ignores
 *   the event.
 */
void MqttPatternChangeEventHandler(int pattern)
{
   gpio_set_level(GPIO_NUM_5, 1); //crude cpu usage monitor

   switch (pattern)
   {
      case (int) PatternGenerator::Pattern::NONE:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::NONE, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      case (int) PatternGenerator::Pattern::HANN_WINDOW_PULSE:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::HANN_WINDOW_PULSE, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      case (int) PatternGenerator::Pattern::HANN_WINDOW_REPEATING:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::HANN_WINDOW_REPEATING, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      case (int) PatternGenerator::Pattern::NOISE:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::NOISE, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      case (int) PatternGenerator::Pattern::MORSE_CODE_SOS:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::MORSE_CODE_SOS, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      case (int) PatternGenerator::Pattern::HALF_SCALED_HANN_WINDOW_PULSE:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::HALF_SCALED_HANN_WINDOW_PULSE, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      case (int) PatternGenerator::Pattern::HALF_SCALED_HANN_WINDOW_REPEATING:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::HALF_SCALED_HANN_WINDOW_REPEATING, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      case (int) PatternGenerator::Pattern::BULK_KNIGHT_RIDER:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::BULK_KNIGHT_RIDER, true);
         m_visualizer.ChangeColorsToRedScale();
         break;

      case (int) PatternGenerator::Pattern::SOLID_FULL_SCALE:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::SOLID_FULL_SCALE, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      case (int) PatternGenerator::Pattern::BULK_SOLID_FIRST_HALF:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::BULK_SOLID_FIRST_HALF, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      case (int) PatternGenerator::Pattern::BULK_SOLID_SECOND_HALF:
         m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::BULK_SOLID_SECOND_HALF, true);
         m_visualizer.ChangeColorsToHeatMap();
         break;

      default:
         //no nothing
         break;
   }
}

/**
 *  InvalidateLastPinValues()
 *    - useful for when MQTT network/connection
 *      goes down/up, so that we can automatically
 *      republish switch/pin states.
 */
void InvalidateLastPinValues()
{
   gpio_set_level(GPIO_NUM_5, 1); //crude cpu usage monitor
   m_GpioMonitor.InvalidateAllPins();
}

/**
 * GpioChangeHandler() - a gpio pin has changed.
 *    We notify MQTT Broker of the change.
 */
void GpioChangeHandler(gpio_num_t pin, int value)
{
   gpio_set_level(GPIO_NUM_5, 1); //crude cpu usage monitor

   int i;
   for(i = 0; i < m_PinsToRead.size(); i++)
   {
      if(m_PinsToRead[i] == pin)
         break;
   }

   MqttClient::PublishSwitchEvent(i, value);
}

/**
 * GpioAnyPinHighLowHandler()
 *   - did any pin being monitored go high?
 *     if so, we will light up any connected LED Strip
 */
void GpioAnyPinHighLowHandler(bool isSomePinHigh)
{
   gpio_set_level(GPIO_NUM_5, 1); //crude cpu usage monitor

   if(isSomePinHigh)
   {
      // might as well light up an LED strip if connected...
      m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::SOLID_FULL_SCALE, true);
      m_visualizer.ChangeColorsToHeatMap();
   }
   else
   {
      m_PatternGenerator.ChangePattern(PatternGenerator::Pattern::NONE, true);
      m_visualizer.ChangeColorsToHeatMap();
   }
}

/**
 *
 */
extern "C" void app_main()
{
   //use GPIO 5 (LED)
   //as crude CPU usage measurement
   gpio_pad_select_gpio(GPIO_NUM_5);
   gpio_set_direction(GPIO_NUM_5, GPIO_MODE_OUTPUT);

   nvs_flash_init();

   ESP_LOGI("main", "starting...");

   //crude cpu check wire up idle hook
   esp_register_freertos_idle_hook(IdleHook);

   internal_tcpip_and_wifi_init(wifi_tcp_event_handler, nullptr);

   //start the visualizer thread/function
   m_visualizer.Init();
   m_visualizer.ChangeColorsToHeatMap();

   //start the pattern generator
   m_PatternGenerator.Start(PatternGenerator::Pattern::HANN_WINDOW_PULSE, 60, 25, PatternGenCallback);

#if defined(CONFIG_ESHTHING_SWITCH_DETECTOR)
   //invalidate the switch gpio pins so that we guarantee that the state
   //of each pin is again published to the MQTT Broker.
   MqttClient::RegisterMqttUpEventHandler(InvalidateLastPinValues);

   m_GpioMonitor.Init(GpioChangeHandler, GpioAnyPinHighLowHandler);
#else
   MqttClient::RegisterPatternEventHandler(MqttPatternChangeEventHandler);
#endif
}
