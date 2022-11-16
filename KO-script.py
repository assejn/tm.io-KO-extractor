import requests
import json
import csv

headers = {'User-Agent': 'describe whatever you do'}
compID = '4059'
matchID = '42213'
refresh = 0

header = ['Points', 'Player', "PlayerID"]
with open('KO-data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    
    while refresh <= 3:
        url = 'https://trackmania.io/api/comp/' + compID + '/match/' + matchID + '/' + str(refresh)
        rawData = requests.get(url, headers=headers).json()
        if 'results' in rawData:
            results = rawData['results']
            if results is not None and len(results) > 0:
                for result in results:
                    player = result['player']
                    playerName = player['name']
                    playerID = player['id']
                    playerRank = result['position']
                    playerData = [playerRank, playerName, playerID]
                    writer.writerow(playerData)
        refresh = refresh + 1