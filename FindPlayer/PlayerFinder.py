import json
import requests

REQ_DICT = {
        "REGION": "na",
        "REGION2" : "NA1",
        "KEY": "",
        "LEAGUE_TYPE" : "RANKED_FLEX_SR"
        }

def get_player_id(player_names):
    if len(player_names) >40:
        raise ValueError("Maximum number of players should not be more than 40.")
    player_names = ','.join(player_names)
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v1.4/summoner/by-name/{NAMES}?api_key={KEY}"
    req = requests.get(URL.format(NAMES = player_names, **REQ_DICT))
    if req.status_code != 200:
        return None
    return json.loads(req.text)

def get_summoner_rank(ids):
    if len(ids) >10:
        raise ValueError("Maximum number of ids shouldn't be more than 10.")
    ids = ','.join(ids)
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v2.5/league/by-summoner/{IDS}/entry?api_key={KEY}"
    req = requests.get(URL.format(IDS = ids, **REQ_DICT))
    if req.status_code != 200:
        return None
    return json.loads(req.text)

def get_league(ids):
    if len(ids) > 10:
        raise ValueError("Maximum nubmer of ids  shouldn't be more than 10.")
    ids = ','.join(ids)
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v2.5/league/by-summoner/{IDS}?api_key={KEY}"
    req = requests.get(URL.format(IDS = ids, **REQ_DICT))
    if req.status_code !=200:
        return None
    return json.loads(req.text)

def get_current_game(summoner_id):
    URL = "https://{REGION}.api.pbp.net/observer-mode/rest/consumer/"
    +"getSpectatorGameInfo/{REGION2}/{id}?api_key={KEY}"
    req = requests.get(URL.format(ID = summoner_id, **REQ_DICT))
    if req.status_code != 200:
        return None
    return json.loads(req.text)

def get_challenger_league():
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v2.5/league/challenger?type={LEAGUE_TYPE}&api_key={KEY}"
    req = reqeusts.get(URL.format(**REQ_DICT))
    if req.status != 200:
        return None
    return json.loads(req.text)

def get_master_league():
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v2.5/league/master?type={LEAGUE_TYPE}&api_key={KEY}"
    req = reqeusts.get(URL.format(**REQ_DICT))
    if req.status != 200:
        return None
    return json.loads(req.text)

def get_recent_games(summoner_id)
    URL = "https://{REGION}.api.pvp.net/api/lol/{REGION}/v1.3/game/by-summoner/{ID}/recent?api_key={KEY}"
    req = requests.get(URL.format(**REQ_DICT))
    if req.status != 200:
        return None
    return json.loads(req.text)

def get

if __name__ == "__main__" :
    with open("info.json", "r") as key_file:
        d = json.load(key_file)
        REQ_DICT["KEY"] = d["apiKey"]
    sum_id = "67030776"
    league = get_league([sum_id])
    entries = league[sum_id][0]["entries"]
    print(len(entries))
    for e in entries:
        if e["playerOrTeamName"].lower()[0] == 'q':
            print("{} {}".format(e["playerOrTeamName"],e["division"]))
