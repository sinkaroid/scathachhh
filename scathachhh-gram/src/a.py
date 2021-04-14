import json

with open('./data/data.json') as f:
  data = json.load(f)

#dumps the json object into an element
json_str = json.dumps(data)

#load the json to a string
resp = json.loads(json_str)

#print the resp
#print (resp)

#extract an element in the response
print(resp['gelbooru'])
#print(asu)