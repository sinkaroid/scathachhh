import json
with open('./data/data.json') as f:
  data = json.load(f)

json_str = json.dumps(data)
resp = json.loads(json_str)

def tokenBot():
    return resp['TOKEN']

def scathach_api():
    return "http://192.145.238.5/~pasirm5/api"

def gelbooru():
    return resp["gelbooru"]

def kona():
    return resp["konachan"]

def r34():
    return resp["r34"]

def loli():
    return resp["lolibooru"]

def rb():
    return resp["realbooru"]

def yande():
    return resp["yandere"]

def tuit():
    return resp["twitter"]

def crypto():
    return resp["cmarket"]