/*
 * MqttClient.cpp
 *
 *  Created on: Jan 1, 2017
 *      Author: eshlemanm

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

#include "MqttClient.h"
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <array>
#include <algorithm>
#include "sdkconfig.h"
extern "C" {
#include "mqtt.h"
}
#include <esp_log.h>

using namespace CoveMountainSoftware;

static constexpr const char * tag = "MqttClient";
static mqtt_settings m_settings;
static mqtt_client * m_client = nullptr;
static MqttClient::PatternEventHandler m_patternEventHandler = nullptr;
static MqttClient::SimpleEventHandler m_mqttUpHandler = nullptr;

static constexpr const char * BaseTopic = "/EshThings";
static constexpr const char * EventsSub = "/Events";
static constexpr const char * StatusSub = "/Status";
static constexpr const char * SwitchSub = "/Switch";

static std::array<char, CONFIG_MQTT_MAX_LWT_TOPIC> m_SwitchStatusTopicBuffer;

#if !defined(CONFIG_ESHTHING_SWITCH_DETECTOR)
static constexpr const char * IndicatorsSub = "/Indicators";
static constexpr const char * PatternSub = "/Pattern";
static std::array<char, CONFIG_MQTT_MAX_LWT_TOPIC> m_IndicatorTopicBuffer;
#endif

/**
 * connected_cb() - MQTT connected handler.
 *   We use this handler to subscribe to
 *   topics upon connection to the MQTT server.
 */
static void connected_cb(void *self, void *params)
{
   ESP_LOGI(tag, "connected_cb");

   m_client = (mqtt_client *) self;

#if defined(CONFIG_ESHTHING_SWITCH_DETECTOR)
   //nothing to subscribe to...
#else
   //must be an "indicator" build...
   m_IndicatorTopicBuffer.fill(0);
   snprintf(m_IndicatorTopicBuffer.data(), m_IndicatorTopicBuffer.size() - 1, "%s%s/%s%s",
         BaseTopic, IndicatorsSub, CONFIG_ESHTHING_MQTT_CLIENTID, PatternSub);

   mqtt_subscribe(m_client, m_IndicatorTopicBuffer.data(), 0);
#endif

   if(m_mqttUpHandler != nullptr)
      m_mqttUpHandler();
}

/**
 * disconnected_cb() - MQTT disconnected handler.
 */
static void disconnected_cb(void *self, void *params)
{
   ESP_LOGI(tag, "disconnected_cb");
   m_client = nullptr;
}

/**
 *
 */
static void reconnect_cb(void *self, void *params)
{
   ESP_LOGI(tag, "reconnect_cb");
}

/**
 *
 */
static void subscribe_cb(void *self, void *params)
{
   ESP_LOGI(tag, "subscribe_cb");
}

/**
 *
 */
static void publish_cb(void *self, void *params)
{
   ESP_LOGI(tag, "publish_cb");
}

/**
 * data_cb() - MQTT data received.
 *    We parse this to handle the expected/possible subscriptions
 *    and activate any registered event handlers.
 */
static void data_cb(void *self, void *params)
{
   ESP_LOGI(tag, "data_cb");

#if defined(CONFIG_ESHTHING_SWITCH_DETECTOR)
   //TBD... maybe nothing
#else
   mqtt_event_data_t *event_data = (mqtt_event_data_t *) params;

   if(0 == strncmp(event_data->topic, m_IndicatorTopicBuffer.data(), event_data->topic_length))
   {
      ESP_LOGI(tag, "pattern topic: len=%d, data = %s", event_data->data_length, event_data->data);

      std::array<char, 12> dataCopy;
      dataCopy.fill(0);
      memcpy(dataCopy.data(), event_data->data, std::min(event_data->data_length, (uint16_t)(dataCopy.size()-1)));

      int value = atoi(dataCopy.data());
      if(m_patternEventHandler)
         m_patternEventHandler(value);
   }
#endif
}

/**
 *
 */
void MqttClient::Start()
{
   ESP_LOGI(tag, "Start");

   strncpy(m_settings.host, CONFIG_ESHTHING_MQTT_SERVER, sizeof(m_settings.host) - 1);
   m_settings.port = 1883; // unencrypted
   strncpy(m_settings.client_id, CONFIG_ESHTHING_MQTT_CLIENTID, sizeof(m_settings.client_id) - 1);
   m_settings.username[0] = 0;
   m_settings.password[0] = 0;
   m_settings.clean_session = 0;
   m_settings.keepalive = 120;
   strncpy(m_settings.lwt_topic, "/lwt", sizeof(m_settings.lwt_topic) - 1);
   strncpy(m_settings.lwt_msg, "offline", sizeof(m_settings.lwt_msg) - 1);
   m_settings.lwt_qos = 0;
   m_settings.lwt_retain = 0;
   m_settings.connected_cb = connected_cb;
   m_settings.disconnected_cb = disconnected_cb;
   m_settings.reconnect_cb = reconnect_cb;
   m_settings.subscribe_cb = subscribe_cb;
   m_settings.publish_cb = publish_cb;
   m_settings.data_cb = data_cb;

   mqtt_start(&m_settings);
}

/**
 *
 */
void MqttClient::Stop()
{
   ESP_LOGI(tag, "Stop");

   mqtt_stop();
}

/**
 *
 */
void MqttClient::RegisterPatternEventHandler(PatternEventHandler handler)
{
   m_patternEventHandler = handler;
}

/**
 *
 */
void MqttClient::RegisterMqttUpEventHandler(SimpleEventHandler handler)
{
   m_mqttUpHandler = handler;
}

/**
 *
 */
void MqttClient::PublishSwitchEvent(uint16_t switchId, uint8_t value)
{
   if(m_client == nullptr)
   {
      ESP_LOGI(tag, "ignoring publish of switch event");
      return;
   }

   std::array<char, 10> valueAsString;
   valueAsString.fill(0);

   snprintf(valueAsString.data(), valueAsString.size() - 1, "%d", value);

   m_SwitchStatusTopicBuffer.fill(0);
   snprintf(m_SwitchStatusTopicBuffer.data(), m_SwitchStatusTopicBuffer.size() - 1, "%s%s/%s%s%d%s",
         BaseTopic, EventsSub, CONFIG_ESHTHING_MQTT_CLIENTID, SwitchSub, switchId, StatusSub);

   mqtt_publish(m_client, m_SwitchStatusTopicBuffer.data(),
         valueAsString.data(), strlen(valueAsString.data()), 1, true);
}
