import requests


class SoraWeb():

    Encoding = "utf-8"
    BaseURL = "https://trailsinthedatabase.com/api/"
    GameURL = "game"
    ScriptFileURL = "file?game_id=%s"
    ScriptsURL = "script/detail/%s/%s"


    def __init__(self):
        pass

    def GetGames(self):
        url = self.BaseURL + self.GameURL
        print("== Getting Games by calling %s%s" % (self.BaseURL, self.GameURL))
        resp = requests.get(url)
        
        #return resp.content.decode(self.Encoding)
        return resp.json()
        
    def getScriptFiles(self, gameId):        
        url = self.BaseURL + (self.ScriptFileURL % gameId)
        print("== Getting script files of game %s" % gameId)
        resp = requests.get(url)
        return resp.json()


    def getScriptFileDetails(self, gameId, fileName):        
        url = self.BaseURL + (self.ScriptsURL % (gameId, fileName))
        print("== Getting details of script file  %s" % fileName)
        resp = requests.get(url)
        return resp.json()


