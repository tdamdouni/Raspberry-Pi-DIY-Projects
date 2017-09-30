import requests

resp = requests.get('https://io.adafruit.com/api/feeds/ping/data', headers={'x-aio-key':'YOUR_ADAFRUIT_API_KEY'})
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

count = 0
ping_list = []
ping_avg = 0


for item in resp.json():
    print('{} {}'.format(item['id'], item['value']))
    count = count + 1
    print('Count: ', count)
    ping_list.append(round(float(item['value']), 3))


ping_avg = round(sum(ping_list)/len(ping_list), 3)

ping_min = ping_list[0]
ping_max = ping_list[0]

for ping in ping_list:
    #print('ping_list value: ', ping)
    if ping < ping_min: 
        ping_min = ping
        #print('new ping_min value: ', ping_min)
    if ping > ping_max: 
        ping_max = ping
        #print('new ping_max value: ', ping_max)
    
avg_url = "https://io.adafruit.com/api/feeds/ping-avg/data"

avg_payload = "{\n\t\"value\":\"" + str(ping_avg) + "\"\n}"
avg_headers = {
    'x-aio-key': "YOUR_ADAFRUIT_API_KEY",
    'content-type': "application/json"
    }

avg_response = requests.request("POST", avg_url, data=avg_payload, headers=avg_headers)

print(avg_response.text)

min_url = "https://io.adafruit.com/api/feeds/ping-min/data"

min_payload = "{\n\t\"value\":\"" + str(ping_min) + "\"\n}"
min_headers = {
    'x-aio-key': "YOUR_ADAFRUIT_API_KEY",
    'content-type': "application/json"
    }

min_response = requests.request("POST", min_url, data=min_payload, headers=min_headers)

print(min_response.text)

max_url = "https://io.adafruit.com/api/feeds/ping-max/data"

max_payload = "{\n\t\"value\":\"" + str(ping_max) + "\"\n}"
max_headers = {
    'x-aio-key': "YOUR_ADAFRUIT_API_KEY",
    'content-type': "application/json"
    }

max_response = requests.request("POST", max_url, data=max_payload, headers=max_headers)

print(max_response.text)
