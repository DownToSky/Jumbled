import json
import requests
import time

REQ_DICT = {
        "REGION": "na",
        "REGION2" : "NA1",
        "KEY": "",
        "LEAGUE_TYPE" : "RANKED_SOLO_5x5"
        }

last_req_time = time.time()
rate = 600/500

def wait_for_api():
    curr = time.time()
    print(last_req_time + rate - curr)
    if last_req_time + rate > curr:
        time.sleep(last_req_time +rate - curr)

def get_player_id(player_names):
    if len(player_names) >40:
        raise ValueError("Maximum number of players should not be more than 40.")
    player_names = ','.join(player_names)
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v1.4/summoner/by-name/{NAMES}?api_key={KEY}"
    time.sleep(rate)
    req = requests.get(URL.format(NAMES = player_names, **REQ_DICT))
    if req.status_code != 200:
        return None
    return json.loads(req.text)

def get_summoner_rank(ids):
    if len(ids) >10:
        raise ValueError("Maximum number of ids shouldn't be more than 10.")
    ids = ','.join(ids)
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v2.5/league/by-summoner/{IDS}/entry?api_key={KEY}"
    time.sleep(rate)
    req = requests.get(URL.format(IDS = ids, **REQ_DICT))
    if req.status_code != 200:
        return None
    return json.loads(req.text)

def get_league(ids):
    if len(ids) > 10:
        raise ValueError("Maximum number of ids  shouldn't be more than 10.")
    ids = ','.join(ids)
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v2.5/league/by-summoner/{IDS}?api_key={KEY}"
    time.sleep(rate)
    req = requests.get(URL.format(IDS = ids, **REQ_DICT))
    if req.status_code !=200:
        return None
    return json.loads(req.text)

def get_current_game(summoner_id):
    URL = "https://{REGION}.api.pbp.net/observer-mode/rest/consumer/"
    +"getSpectatorGameInfo/{REGION2}/{id}?api_key={KEY}"
    time.sleep(rate)
    req = requests.get(URL.format(ID = summoner_id, **REQ_DICT))
    if req.status_code != 200:
        return None
    return json.loads(req.text)

def get_challenger_league():
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v2.5/league/challenger?type={LEAGUE_TYPE}&api_key={KEY}"
    time.sleep(rate)
    req = requests.get(URL.format(**REQ_DICT))
    if req.status_code != 200:
        return None
    return json.loads(req.text)

def get_master_league():
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v2.5/league/master?type={LEAGUE_TYPE}&api_key={KEY}"
    time.sleep(rate)
    req = requests.get(URL.format(**REQ_DICT))
    if req.status_code != 200:
        return None
    return json.loads(req.text)

def get_recent_games(summoner_id):
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v1.3/game/by-summoner/{ID}/recent?api_key={KEY}"
    time.sleep(rate)
    req = requests.get(URL.format(ID = summoner_id , **REQ_DICT))
    if req.status_code != 200:
        return None
    return json.loads(req.text)

if __name__ == "__main__" :
    with open("info.json", "r") as key_file:
        d = json.load(key_file)
        REQ_DICT["KEY"] = d["apiKey"]
    """ 1
    ch = get_challenger_league()
    ma = get_master_league()
    summonerIdsToCheck = dict()
    for e in ch['entries']:
        summonerIdsToCheck[str(e['playerOrTeamId'])] = e['playerOrTeamName']
    for e in ma['entries']:
        summonerIdsToCheck[str(e['playerOrTeamId'])] = e['playerOrTeamName']
    potPlats = set()
    for playerId in summonerIdsToCheck:
        games = get_recent_games(playerId)
        for game in games["games"]:
            if "RANKED_SOLO_5x5" in game["subType"]:
                if "fellowPlayers" in game:
                    for player in game["fellowPlayers"]:
                        potPlats.add(str(player["summonerId"]))
                        print(player["summonerId"])
    with open("potPlat.txt",'w') as potFile:
        potFile.write("\r\n".join(potPlats))
    """
    """
    potPlats = set()
    with open("potPlat.txt",'r')as potFile:
        for line in potFile:
            potPlats.add(line.strip())
    potPlats = list(potPlats)
    potPlats = [potPlats[x:x+10] for x in range(0, len(potPlats),10)]
    PlatDivs = set()
    Plats = dict()
    for ids in potPlats:
        leagues = get_league(ids)
        for ID in ids:
            if ID not in leagues:
                continue
            if leagues[ID][0]["queue"] != "RANKED_SOLO_5x5":
                print("NOT RANKED SOLO 5X5 "+ID)
            if leagues[ID][0]["tier"] == "PLATINUM":
                if not leagues[ID][0]["name"] in PlatDivs:
                    print(leagues[ID][0]["name"])
                    PlatDivs.add(leagues[ID][0]["name"])
                    for player in leagues[ID][0]["entries"]:
                        Plats[player["playerOrTeamId"]] = player["playerOrTeamName"]
                print(len(Plats))
    with open("plats.json", 'w') as platsF:
        json.dump(Plats,platsF)
    with open("platDivs.json" , 'w')as divsF:
        json.dump(list(PlatDivs), divsF)
    print("total divisions: {} total plat players: {}".format(len(PlatDivs), len(Plats)))
    """


    Plats = set()
    PlatDivs = dict()
    with open("plats.json", 'r') as platF:
        Plats =json.load(platF)
    with open("platDivs.json", 'r')as divsF:
        PlatDivs = set(json.load(divsF))
    Plats = [val for val in Plats]
    Plats = [Plats[x:x+10] for x in range(0, len(Plats), 10)]
    for ids in Plats:
        leagues = get_league(ids)
        if leagues != None:
            continue
        for ID in ids:
            if ID not in leagues:
                continue
            if leagues[ID][0]["queue"] != "RANKED_SOLO_5x5":
                print("NOT RANKED SOLO 5X5 "+ID)
            if leagues[ID][0]["tier"] == "PLATINUM":
                if not leagues[ID][0]["name"] in PlatDivs:
                    for player in leagues[ID][0]["entries"]:
                        if player["playerOrTeamName"].lower()[0] == "q":
                            if player["division"] == "III":
                                print(player["playerOrTeamName"])
                        else:
                            print(player["playerOrTeamName"])
