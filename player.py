import requests
import json
import os 

class Player:
    def __init__(self, data):
        self.__update_player_details(data)
    
    def __update_player_details(self, data):
        self.username = data["username"]
        self.kills = data["lifetime"]["mode"]["br_all"]["properties"]["kills"]
        self.deaths = data["lifetime"]["mode"]["br_all"]["properties"]["deaths"]
        self.kd_ratio = data["lifetime"]["mode"]["br_all"]["properties"]["kdRatio"]


    def __repr__(self):
        return f'<Player { self.username } | kills: { self.kills } | deaths { self.deaths } | KDR { round(self.kd_ratio,3) }>'

    @classmethod
    def __get_player_data(self, tag):
        cookies = {"ACT_SSO_COOKIE":os.getenv("COD_COOKIE")}
        r = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/{}/profile/type/wz'.format(tag.replace("#","%23")), cookies=cookies)
        return r.content

    @classmethod
    def from_battletag(cls, tag):
        player_data = cls.__get_player_data(tag)
        json_dict = json.loads(player_data)
        return cls(json_dict["data"])

    def refresh_stats(self):
        data = Player.__get_player_data(self.username)
        self.__update_player_details((json.loads(data))["data"])
