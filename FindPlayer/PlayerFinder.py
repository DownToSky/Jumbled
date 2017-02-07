import json
import requests
import time
import copy

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
    #print(URL.format(IDS = ids , **REQ_DICT))
    req = requests.get(URL.format(IDS = ids, **REQ_DICT))
    if req.status_code !=200:
        return None
    return json.loads(req.text)

def get_plat_leagues(ids):
    leagues = get_league(ids)
    c = 0
    while leagues == None and c<5:
        leagues = get_league(ids)
        print("NONE")
        c+=1
    if leagues == None:
        return None
    plats = dict()
    for ID in ids:
        if ID in leagues:
            if leagues[ID][0]["queue"] == "RANKED_SOLO_5x5" and leagues[ID][0]["tier"] == "PLATINUM":
                league_name = leagues[ID][0]["name"]
                plats[league_name]=dict()
                plats[league_name]["I"] = dict()
                plats[league_name]["II"] = dict()
                plats[league_name]["III"] = dict()
                plats[league_name]["IV"] = dict()
                plats[league_name]["V"] = dict()
                for player in leagues[ID][0]["entries"]:
                    plats[league_name][player["division"]][player["playerOrTeamId"]] = player["playerOrTeamName"]
    return plats

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
    Plats = dict()
    for ids in potPlats:
        leagues = get_league(ids)
        for ID in ids:
            if ID not in leagues:
                continue
            i = 0
            for i in range(0,len(leagues[ID])):
                if leagues[ID][i]["queue"] != "RANKED_SOLO_5x5":
                    print("NOT RANKED SOLO 5X5 "+ID)
                else:
                    break
            if leagues[ID][i]["tier"] == "PLATINUM":
                league_name = leagues[ID][i]["name"]
                if not league_name in Plats:
                    print(league_name)
                    Plats[league_name] = dict()
                    Plats[league_name]['I'] = dict()
                    Plats[league_name]['II'] = dict()
                    Plats[league_name]['III'] = dict()
                    Plats[league_name]['IV'] = dict()
                    Plats[league_name]['V'] = dict()
                    c = 0
                    for player in leagues[ID][i]["entries"]:
                        c+=1
                        Plats[league_name][player["division"]][player["playerOrTeamId"]]=player["playerOrTeamName"]
                    print(c)
    with open("plats.json", 'w') as platsF:
        json.dump(Plats,platsF)
    """
    """
    Plats = set()
    PlatDivs = dict()
    with open("plats.json", 'r') as platF:
        Plats =json.load(platF)
    with open("platDivs.json", 'r')as divsF:
        PlatDivs = set(json.load(divsF))
    PlatDivs = set()
    Plats = [val for val in Plats]
    Plats = [Plats[x:x+10] for x in range(0, len(Plats), 10)]
    for ids in Plats:
        leagues = get_league(ids)
        if leagues == None:
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
                            if player["division"] == "II":
                                PlatDivs.add(leagues[ID][0]["name"])
                                print(player["playerOrTeamName"])
    """

    plats = dict()
    with open("plats.json", 'r')as platF:
        plats = json.load(platF)
    newPlats = copy.deepcopy(plats)
    for n in plats:
        for d in plats[n]:
            for p in plats[n][d]:
                games = get_recent_games(p)
                if games == None or "games" not in games:
                    print("GAME NOT FOUND")
                    continue
                for game in games["games"]:
                    if game["subType"] == "RANKED_SOLO_5x5":
                        idsToCheck = list()
                        for player in game["fellowPlayers"]:
                            idsToCheck.append(str(player["summonerId"]))
                        tmp = get_plat_leagues(idsToCheck)
                        if tmp == None:
                            print("NONE")
                            continue
                        c = 0
                        for divName in tmp:
                            if divName not in newPlats:
                                c+=1
                                newPlats[divName] = tmp[divName]
                                print(tmp[divName]["II"])
                            else:
                                print("DIV NAME ALREADY EXISTS")
                        if c>0:
                            with open("newPlats.json", 'w')as newPlatF:
                                json.dump(newPlats , newPlatF)
    with open("newPlats.json", 'w')as newPlatF:
        json.dump(newPlats , newPlatF)
