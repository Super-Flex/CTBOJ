import requests, json
from time import sleep


def problemInfo_return_key(problem_id):
    URL = f"https://solved.ac/api/v3/problem/lookup?problemIds={problem_id}"
    request = requests.get(URL)
    sleep(1)
    if request.status_code == 429:
        raise 429
    problem = json.loads(request.content.decode("utf-8"))[0].get("tags")
    level = json.loads(request.content.decode("utf-8"))[0].get("level")
    keys = []
    for i in problem:
        # print(i)
        # print(i.get("key"))
        keys.append(i.get("key"))
    return keys, level


print(problemInfo_return_key(16236))
