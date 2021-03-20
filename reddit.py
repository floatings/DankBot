import requests
import re
from datetime import datetime


def makeregex(keys):
    regex = 'r"'
    for word in keys:
        regex += "\\b" + word + "\\b"
        if word != keys[-1]:
            regex += "|"
    return regex


def webauth(auth, data, headers, reddit):
    if (reddit =='a'):
        reddit = subreddit[0]
    elif (reddit == 'b'):
        reddit = subreddit[1]
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
    webname = "https://oauth.reddit.com/r/" + reddit
    return requests.get(webname, headers=headers, params={'limit': '50'})


def searchposts(res, keywords):
    found = []
    thistime = datetime.now()
    i = 1
    for p in res.json()['data']['children']:
        title = str(i) + ". " + "**" + p['data']['title'] + "**"
        if(re.findall(makeregex(keywords),title.lower())):
            site = "https://www.reddit.com/"
            diff = thistime - datetime.fromtimestamp(int(p['data']['created_utc']))
            title += " - " + str(diff)[:4] + "\n" + site + p['data']['permalink'] + " - " + "("\
            + p['data']['author'] + ")\t" + str(p['data']['num_comments']) + " Comments "
            found += [title]
            i = i+1
    return found


auth = requests.auth.HTTPBasicAuth('auth', 'auth')
data = {'grant_type': 'password',
        'username': 'userauth',
        'password': 'passauth'}

headers = {'User-Agent': 'ShopBot/0.0.1'}
keywords_a = ("south bay", "ca", "california", "san jose", "bay area")
keywords_b = ("milkshake", "deskpad", "deskmat")
subreddit = ['aquaswap/new','mechmarket/new']

#for key in p['data'].keys():
#    print(key)

