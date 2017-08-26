/*
 * wifi_init.c
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

#include "freertos/FreeRTOS.h"
#include "esp_wifi.h"
#include "esp_system.h"
#include "esp_event.h"
#include "esp_event_loop.h"
#include "nvs_flash.h"
#include "driver/gpio.h"
#include <esp_log.h>

/**
 * internal_tcpip_and_wifi_init()
 *   Standard ESP-IDF startup for TCP-IP and WIFI.
 */
void internal_tcpip_and_wifi_init(system_event_cb_t cb, void *ctx)
{
   ESP_LOGI("main", "tcpip wifi init...");

   tcpip_adapter_init();
   ESP_ERROR_CHECK(esp_event_loop_init(cb, ctx));
   wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();

   ESP_ERROR_CHECK(esp_wifi_init(&cfg));
   ESP_ERROR_CHECK(esp_wifi_set_storage(WIFI_STORAGE_RAM));
   ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
   wifi_config_t sta_config = {
         .sta = {
               .ssid = CONFIG_ESHTHING_WIFI_SSID,
               .password = CONFIG_ESHTHING_WIFI_PASSWORD,
               .bssid_set = false
         }
   };
   ESP_ERROR_CHECK(esp_wifi_set_config(WIFI_IF_STA, &sta_config));
   ESP_ERROR_CHECK(esp_wifi_start());
   ESP_ERROR_CHECK(esp_wifi_connect());

   ESP_LOGI("main", "tcpip wifi init done");
}
