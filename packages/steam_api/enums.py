from enum import Enum


class DotaID(Enum):
    dota2 = 570
    dota2_beta = 205790
    dota2_internal_test = 816


class SteamUser(Enum):
    method_group = 'ISteamUser'
    method_name = {
        'PlayerSummaries': 'GetPlayerSummaries',
    }


class CosmeticItem(Enum):
    method_group = 'IEconItems_{id}'
    method_name = {
        # todo: not done
        'Schema': 'GetSchemaURL' or 'GetSchema',  # under construction, but currently working getschemaurl
    }


class Match(Enum):
    method_group = 'IDOTA2Match_{id}'
    method_name = {
        'LeagueListing': 'GetLeagueListing',
        'LiveLeagueGames': 'GetLiveLeagueGames',
        'MatchDetails': 'GetMatchDetails',
        'MatchHistory': 'GetMatchHistory',
        'MatchHistoryBySequenceNum': 'GetMatchHistoryBySequenceNum',
        'ScheduledLeagueGames': 'GetScheduledLeagueGames',
        'TeamInfoByTeamID': 'GetTeamInfoByTeamID',
        'TournamentPlayerStats': 'GetTournamentPlayerStats',
        # 'TopLiveGame': 'GetTopLiveGame',  # under construction
    }


class Economy(Enum):
    method_group = 'IEconDOTA2_{id}'
    method_name = {
        'GameItems': 'GetGameItems',
        # 'ItemIconPath': 'GetItemIconPath',   # under construction
        'Heroes': 'GetHeroes',
        'Rarities': 'GetRarities',
        'TournamentPrizePool': 'GetTournamentPrizePool',
        # 'EventStatsForAccount': 'GetEventStatsForAccount',   # under construction
    }
