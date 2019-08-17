import json
import requests

from django.conf import settings

from . import enums
from json.decoder import JSONDecodeError

json_decoder = json.JSONDecoder
json_encoder = json.JSONEncoder

"""under construction:
    1) IDOTA2MatchStats_
    2) IDOTA2Fantasy_
    3) IDOTA2StreamSystem_
    4) IDOTA2Teams_
    4) IDOTA2AutomatedTourney_
    4) IDOTA2Ticket_

    doc url: https://wiki.teamfortress.com/wiki/WebAPI#Dota_2
"""


def get_steam_api_url(method_group, method_name):
    return settings.STEAM_WEB_API_URL.format(method_group=method_group, method_name=method_name)


def check_required_kwargs(**kwargs):
    if not kwargs['key']:
        raise KeyError("Key is required")


class BaseSteamApi(object):
    _url = None
    _timeout = 120  # seconds

    def __init__(self, **kwargs):
        kwargs['key'] = settings.STEAM_WEB_API_KEY  # todo: every call should have a 'key'
        check_required_kwargs(**kwargs)
        self._params = self.create_params(**kwargs)
        if not self._url:
            raise EnvironmentError("Pass a valid url")

    @staticmethod
    def create_params(**kwargs):
        return {
            'format': 'json',
            **kwargs
        }

    def get_response(self):
        try:
            req = requests.get(self._url, params=self._params, timeout=self._timeout)
            print(req.url)
            print(self._params)
            print("Response: \n{}".format(req.text))
            if req.status_code == 200:
                try:
                    _data = json.loads(req.text)
                    return _data
                except JSONDecodeError as er:
                    # todo: show error msg from steamAPI (convert html)
                    print(er)
            else:
                print("Error status! Code: {}".format(req.status_code))
        except requests.exceptions.RequestException as err:
            print("Request error: {}".format(err))
        return None


class PlayerSummaries(BaseSteamApi):
    def __init__(self, steamid, **kwargs):
        """
        example data: ['04136783245678826', '76561198047041318']
        :param steamid: 64 bit steam ID. can be used as list or string
        """
        if isinstance(steamid, list):
            steamid = json.dumps(steamid)
        self._url = get_steam_api_url(enums.SteamUser.method_group.value, enums.SteamUser.method_name.value['PlayerSummaries'])
        kwargs['steamids'] = steamid
        super().__init__(**kwargs)


# for some reason it's not updated
# todo: it's should be updated upon update by valve
class LeagueListing(BaseSteamApi):
    def __init__(self, **kwargs):
        self._url = get_steam_api_url(enums.Match.method_group.value.format(id=enums.DotaID.dota2_beta.value), enums.Match.method_name.value['LeagueListing'])
        super().__init__(key=settings.STEAM_WEB_API_KEY, **kwargs)


class LiveLeagueGames(BaseSteamApi):
    def __init__(self, **kwargs):
        self._url = get_steam_api_url(
            enums.Match.method_group.value.format(id=enums.DotaID.dota2.value),
            enums.Match.method_name.value['LiveLeagueGames']
        )
        super().__init__(key=settings.STEAM_WEB_API_KEY, **kwargs)


pass
