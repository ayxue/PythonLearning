import os
import json
import time
import operator as op
from Sora.SoraWeb import *
import pandas as pd


#SOURCE = "web"
SOURCE = "file"


# Games
def LoadGames(client):
    file = "storages/games.csv"
    if SOURCE == "web":
        jsonGames = client.GetGames()
        games = pd.DataFrame(jsonGames)
        games.to_csv(file, mode="w+", encoding="utf_8_sig", header=True)
        print("====== Games saved...")
    else:
        games = pd.read_csv(file)
    print(games)
    return games


# ScriptFiles
def LoadScriptFiles(client, game):
    print("====== Getting Script files of %s" % game["titleEng"])
    gameId = game.iloc[0]["id"]
    file = "storages/ScriptFilesOfGame_%s.csv" % gameId
    if SOURCE == "web":
        jsonScriptFiles = client.getScriptFiles(gameId)
        scriptFiles = pd.DataFrame(jsonScriptFiles)
        scriptFiles.to_csv(file, mode="w+", encoding="utf_8_sig", header=True)
        print("====== Script files of Game %s saved..." % gameId)
    else:
        scriptFiles = pd.read_csv(file)
    print(scriptFiles)
    return scriptFiles

# Script
def LoadScriptDetails(client, scriptFile):
    gameId = scriptFile["gameId"]
    scriptFileName = scriptFile["fname"]
    file = "storages/Script_Game_%s_%s.csv" % (scriptFileName, gameId)
    #if SOURCE == "web":
    if not os.path.exists(file):
        jsonScript = client.getScriptFileDetails(gameId, scriptFileName)
        scriptFiles = pd.DataFrame(jsonScript)
        scriptFiles.to_csv(file, mode="w+", encoding="utf_8_sig", header=True)
        print("====== Script %s saved..." % scriptFileName)
    else:
        scriptFiles = pd.read_csv(file)
    #print(scriptFiles)
    return scriptFiles


if __name__ == '__main__':
    print("=== Start gethering Sora...")
    client = SoraWeb()

    # Games
    games = LoadGames(client)    
    targetGames = ["Trails in the Sky SC"]

    # ScriptFiles    
    for gameName in targetGames:
        game = games[games["titleEng"] == gameName]
        if game.count == 0:
            print("====== Game %s not found" % gameName)
            continue

        scriptFiles = LoadScriptFiles(client, game)

    # Scripts
    for index, row in scriptFiles.iterrows():
        LoadScriptDetails(client, row)
        print("====== Index %s saved, %s in all ..." % (index, scriptFiles.shape[0]))
        time.sleep(0.7)

        


