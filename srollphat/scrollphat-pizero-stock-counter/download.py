import requests
import json
import time

class download:
    def __init__(self):
        self.base_url = "http://stockalert.alexellis.io/stock/"
        
    def get_total_stock(self, shop):
        url = self.base_url + shop
        print (url)
        resCode = 0
        while(resCode!=200):
            res = requests.get(url)
            resCode = res.status_code
            print("HTTP/" + str(resCode))
            time.sleep(0.5)

        json_data = json.loads(res.text)
        if(json_data["stock"] == True):
            return json_data["totalAmount"]
        return 1

download()
