import json
import os



USER = "252523445206646785"
if __name__ == "__main__":
    logs = dict()
    path = "C:\\Users\\Crimson Phoenix\\Documents\\Jumbled\\MessageSpouter\\degensServerLogs.json"
    outPath = "C:\\Users\\Crimson Phoenix\\Documents\\Jumbled\\MessageSpouter\\outputs.json"
    with open(path, 'r', encoding='utf-8') as f:
        logs = json.load(f)
    user_index = logs["meta"]["userindex"].index(USER)
    messages = dict()
    for channel in logs["data"]:
        for message in logs["data"][channel]:
            if logs["data"][channel][message]["u"] == user_index:
                messages[message] = logs["data"][channel][message]
    with open(outPath, 'w') as f:
        json.dump(messages, f)