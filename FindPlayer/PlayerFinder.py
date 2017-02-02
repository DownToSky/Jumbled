import aiohttp
import json

req_dict = {
        REGION: "na",
        KEY: ""
        }

def get_player_id(player_name):
    pass


if __name__ == "__main__" :
    with open("info.json", "r") as key_file:
        d = json.load(key_file)
        req_dict = d["apiKey"]
    playObj = get_player_id("Q")
