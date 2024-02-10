import requests

url = "https://nicknamegenerator.p.rapidapi.com/api/nick-names"


def get_nick():
    # querystring = {"gender": "male", "group": "superhero"}
    querystring = {"gender": "random", "group": "game"}

    headers = {
        "X-RapidAPI-Key": "3f1905b9d0mshddc1de41f254d76p19826bjsn4e782012a4bb",
        "X-RapidAPI-Host": "nicknamegenerator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()
    res = response['body']
    return res
