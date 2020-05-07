import requests,json 

class Weather():
    @staticmethod
    def get_data(locationName):
        url=("https://opendata.cwb.gov.tw/api/v1/rest/datastore/"
            "F-C0032-001?Authorization=CWB-0FC54884-FCEA-4D0C-98E0-DB0A495D752D"
            "&locationName={locationName}&format=JSON").format(locationName=locationName)
        response=requests.get(url)
        weatherJson = json.loads(response.text)
        weatherData=[]
        for i in range(0,5):
            weatherData.append(
                weatherJson["records"]["location"][0]["weatherElement"]
                [i]["time"][0]["parameter"]['parameterName'])
        return weatherData

# print(Weather.get_data("臺中市"))