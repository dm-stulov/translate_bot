import requests


def translate(word_fron_bot):
    URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
    URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
    KEY = 'NTdhMzkxYW***************WYxZmEwNGZkYjQwMmQ4NDgxOTE0OWQ0NDU5OWY0'

    headers_auth = {'Authorization': 'Basic ' + KEY}

    auth = requests.post(URL_AUTH, headers=headers_auth)

    if auth.status_code == 200:
        token = auth.text
        word = word_fron_bot
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            req = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = req.json()

            try:
                return (res['Translation']['Translation'])
            except:
                return ("no variable to translate")
    else:
        print("Error: " + str(auth.status_code))
