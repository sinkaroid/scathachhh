import json
with open('./data/handle.json') as h:
  handle = json.load(h)

msg = json.dumps(handle)
lahNgatur = json.loads(msg)

def ErrorFlag():
    return lahNgatur['noresult']

def ngaturArgs():
    return lahNgatur['noargs']

def ngaturInvalid():
    return lahNgatur['nocommand']

def ngaturEnggaktau():
    return lahNgatur['enggaktau']

def ngaturNglantur():
    return lahNgatur['embuh']

def ngaturNani():
    return lahNgatur['nani']

def ngaturLawak():
    return lahNgatur['hey']

def ngaturSopan():
    return lahNgatur['pls']

def ngaturHelp():
    return open("./data/help.txt", "r")

def ngaturAli():
    return open("./data/alias.txt", "r")

def successMsg():
    return lahNgatur['200']

def badrequestMsg():
    return lahNgatur['404']

def nekos():
    return lahNgatur['nekos']

def occurred():
    return lahNgatur['wrong']

def randObj():
    return lahNgatur['randomstr']

def splitBoy():
    return lahNgatur['split']

def badHero():
    return lahNgatur['badhero']

def msgEmpty():
    return lahNgatur['empty']

def cantDemote():
    return lahNgatur['demote']

def notModified():
    return lahNgatur['notmodif']

def cantDel():
    return lahNgatur['cantrm']

def deleteNotfound():
    return lahNgatur['rmnotf']

def unAuth():
    return lahNgatur['unauth']

def invalidQuery():
    return lahNgatur['invalidquery']

def tgAPIErr():
    return lahNgatur['TelegramAPIError']

def retryAfter():
    return lahNgatur['retryafter']

def cantParse():
    return lahNgatur['cantparse']