import requests
from time import sleep

urlBase = 'http://localhost:8001/_ah/api/ivchecker/v1'

class TestClass:

    def test_api(self):
        response = requests.get(url='{}/{}'.format(urlBase,'helloWorld'))
        assert response.status_code == 200
        assert response.json().get('content') == 'Hello World!'

    def test_emtpy_get(self):
        # With any verb in the data store:
        response = requests.get(url='{}/{}'.format(urlBase, 'verbs'))
        assert response.status_code == 404  # TODO: Must be a 204

    def test_get_post_delete(self):

        verb = {
            'infinitive': 'be',
            'pastSimple': 'was',
            'pastParticiple': 'been',
            'difficultyLevel': 2
        }

        response = requests.post(url='{}/{}'.format(urlBase, 'verbs'), json=verb)
        assert response.status_code == 200
        verb_saved = response.json()

        for k, v in verb.items():
            assert verb_saved[k] == v

        sleep(0.5)

        # Check the verb has been saved:
        response = requests.get(url='{}/{}'.format(urlBase, 'verbs'))
        assert response.status_code == 200
        verbs = response.json()['verbs']
        assert len(verbs) == 1

        verb_saved = verbs[0]

        for k, v in verb.items():
            assert verb_saved[k] == v

        # Test delete
        response = requests.delete(url='{}/verbs/{}'.format(urlBase, verb_saved['verbId']))
        assert response.status_code == 200

        sleep(0.5)

        response = requests.get(url='{}/{}'.format(urlBase, 'verbs'))
        assert response.status_code == 404  # TODO: Must be a 204
