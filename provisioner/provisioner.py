import requests

urlBase = 'http://localhost:8001/_ah/api/ivchecker/v1'

verb = {
    'infinitive': 'be',
    'pastSimple': 'was',
    'pastParticiple': 'been',
    'difficultyLevel': 1
}

def prov():
    for a in range(10):
        verb['difficultyLevel'] == 1
        response = requests.post(url='{}/{}'.format(urlBase, 'verbs'), json=verb)
        verb['difficultyLevel'] == 2
        response = requests.post(url='{}/{}'.format(urlBase, 'verbs'), json=verb)
        verb['difficultyLevel'] == 3
        response = requests.post(url='{}/{}'.format(urlBase, 'verbs'), json=verb)



if __name__ == "__main__":
    prov()