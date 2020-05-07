from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from get_weather import Weather

class ActionReplyWeather(Action):
    def name(self) -> Text:
        return "action_reply_weather"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("city")
        
        # 由於氣象局API皆使用"臺"一字，為了避免user使用"台"字造成API查詢錯誤，在這邊更正
        # 也可以在語料階段直接將"台"匹配成"臺"，如[台北](city:臺北)
        # 這邊為了降低語料方面的工作量，直接透過custon actions用程式解決。
        if city[0]=="台":
             city = "臺"+city[1:] 

        data=Weather.get_data(city)
        dispatcher.utter_message(
            "{city}的天氣為{wx},降雨機率{pop}%,溫度為{min}°C至{max}°C".format(
                city=city,wx=data[0],pop=data[1],min=data[2],max=data[4]))
        return []


