from time import sleep
import requests
import json
import unittest


def get_MET_weather_observations(location):
    """ From the UK MET Office website documentation:
    Example: to obtain observations for a specified location at all available times in XML format:
    For json:
    http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/[LocationID]?res=hourly&key=<API key>
    Or for XML data return:
    http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/xml/[LocationID]?res=hourly&key=<API key>
    """
    API_key = "238ccea7-66bf-44cf-8b14-b0d7b2d787bf"

    query_url = "http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/{0}?res=hourly&key={1}".format(location, API_key)
    response = requests.get(query_url)

    if response.status_code != 200:
        print("I failed with code ".format(response.status_code))

    data = response.json()
    # print(json.dumps(data, sort_keys=True, indent=4))
    return data

def extract_latest_temperature(temp_list):
    output = [float(s) for s in temp_list]
    return output[24]


def extract_API_temperatures(MET_data):
    output=[]
    main = MET_data["SiteRep"]["DV"]["Location"]["Period"]

    for i in range(len(main)):
        extract_rep = main[i]["Rep"]
        for j in range(len(extract_rep)):
            extract_temperature = extract_rep[j]["T"]
            output.append(extract_temperature)

    return output


if __name__ == "__main__":
    Andrews_Field = "3684"  # Get data from here since it's closest to
    # my geographic location in Cambridge at the moment.
    latest_temp_history = extract_API_temperatures(get_MET_weather_observations(Andrews_Field))
    display_temp = extract_latest_temperature(latest_temp_history)
    print(display_temp)
