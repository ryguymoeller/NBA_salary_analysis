import json
import requests
import sys
import pprint
import datetime

url = 'https://www.balldontlie.io/api/v1/stats?seasons[]=2019&dates[]=2019-10-22'

response = requests.get(url)
response.raise_for_status()
NBAdata = json.loads(response.text)
stats = NBAdata['data']
playerList = {}
for player in stats:
    playerid = player['player']['id']
    playerFirst = player['player']['first_name']
    playerLast = player['player']['last_name']
    playerAst = player['ast']
    playerList.setdefault(playerid, {'first': playerFirst, 'last': playerLast, 'ast': playerAst})

print(playerList)
