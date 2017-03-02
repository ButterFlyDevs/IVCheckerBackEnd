import requests

urlBase = 'http://localhost:8080/_ah/api/ivchecker/v1'


class TestClass:

    def test_api(self):
        response = requests.get(url='{}/{}'.format(urlBase,'helloWorld'))
        assert response.status_code == 200
        assert response.json().get('content') == 'Hello World!'
