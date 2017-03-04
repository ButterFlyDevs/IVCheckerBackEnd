"""This is ivchecker API implemented using Google Cloud Endpoints."""

# [START imports]
import endpoints
from google.appengine.ext import ndb
from protorpc import message_types
from protorpc import messages
from protorpc import remote

from messages.messages import Verb as verb_message, VerbsList as verbs_list_message, EchoResponse
from models.verb_model import Verb as verb_db_model
# [END imports]


GET_RESOURCE = endpoints.ResourceContainer(
    # The request body should be empty.
    message_types.VoidMessage,
    # Accept two url parameter: an integer named 'url_param_a' and another named 'url_param_b'
    url_param_a=messages.StringField(1),
    url_param_b=messages.StringField(2))

GET_RESOURCE2 = endpoints.ResourceContainer(message_types.VoidMessage,
                                            id=messages.IntegerField(1, variant=messages.Variant.INT32))


# [START echo_api]
@endpoints.api(name='ivchecker', version='v1')
class IVCheckerApi(remote.Service):

    @endpoints.method(message_types.VoidMessage, EchoResponse, path='helloWorld', http_method='GET', name='helloWorld')
    def echo_api_key(self, request):
        return EchoResponse(content='Hello World!')

    # TODO: Join all verb/ GET related methods in one endpoint resource and only one function instead of few.
    @endpoints.method(GET_RESOURCE, verbs_list_message,
                      path='verbs/{url_param_a}/{url_param_b}', http_method='GET', name='verbs.difficulty')
    def get_verbs_difficulty(self, request):
        """
        Get all verbs in the data store with (without examples) the same difficulty.

        .../verbs/difficulty/d all verbs without examples with this difficulty

        :param request:
        :return: A kind of message verbs_list_message
        """

        difficulty_level = int(request.url_param_b)

        # .../verbs/n
        if request.url_param_a == 'difficulty' and difficulty_level >=1 and difficulty_level <=3:

            query = verb_db_model.query(verb_db_model.difficultyLevel == difficulty_level)

            num_verbs = query.count()
            print num_verbs
            if num_verbs > 0:
                print num_verbs
                verbs_list = []
                for verb in query.iter():
                    verb_id = verb._key.id()
                    verb_dict = verb.to_dict()

                    print verb_dict

                    verbs_list.append(verb_message(verbId=verb_id, infinitive=verb_dict['infinitive'],
                                 pastSimple=verb_dict['pastSimple'], pastParticiple=verb_dict['pastParticiple']))

                return verbs_list_message(verbs=verbs_list)
            else:
                raise endpoints.NotFoundException('Verbs with difficulty {} not found'.format(difficulty_level))
        else:
            raise endpoints.NotFoundException('Verbs with difficulty {} not found'.format(difficulty_level))

    @endpoints.method(GET_RESOURCE2, verb_message, path='verbs/{id}', http_method='GET', name='verbs.get')
    def get_verb(self, request):
        """
        Get a specific verb with all info about it.

        Examples:
            .../verbs/n  give all info about a verb, included extra info like examples of use.

        :param request:
        :return: A verb_message info object with all info about this verb
        """
        # All info about specific verb
        if request.id :

            key = ndb.Key('Verb', long(request.id))
            verb = verb_db_model.query(verb_db_model.key == key).get()

            if verb:
                verb = verb.to_dict()
                return verb_message(verbId = key.id(), infinitive=verb['infinitive'],
                                pastSimple=verb['pastSimple'], pastParticiple=verb['pastParticiple'],
                                difficultyLevel=verb['difficultyLevel'], examples=verb.get('examples', None))
            else:
                raise endpoints.NotFoundException('Verb {} not found'.format(request.id))


    @endpoints.method(message_types.VoidMessage, verbs_list_message, path='verbs', http_method='GET', name='verbs.getOne')
    def get_verbs(self, request):
        """
        Return a list with all verbs in the data store.

        :param request:
        :return:
        """

        query = verb_db_model.query()

        num_verbs = query.count()
        if num_verbs > 0:
            print num_verbs
            verbs=[]
            for verb in query.iter():
                verb_id = verb._key.id()
                verb_dict = verb.to_dict()
                verbs.append(verb_message(verbId=verb_id, infinitive=verb_dict['infinitive'],
                             pastSimple=verb_dict['pastSimple'], pastParticiple=verb_dict['pastParticiple'],
                             difficultyLevel=verb_dict['difficultyLevel']))

            return verbs_list_message(verbs=verbs)

        # If there aren't any verb:
        else:
            # TODO: It must be return a 204 status code error.
            raise endpoints.NotFoundException('Verbs collection is empty')

    @endpoints.method(verb_message, verb_message, path='verbs', http_method='POST', name='verbs.insert')
    def post_verbs(self, request):

        """
        Examples of use with curl
        curl -i -d "infinitive=puta&pastSimple=b&pastParticiple=ks&difficultLevel=4" -X POST -G  http://localhost:8080/_ah/api/ivchecker/v1/verbs
        echo -n '{"infinitive": "ola"}' | curl --header "Content-pe:application/json" -X POST -d  @- http://localhost:8080/_ah/api/ivchecker/v1/verbs

        :param request:
        :return:
        """

        verb = verb_db_model(infinitive=request.infinitive, pastSimple=request.pastSimple,
                             pastParticiple=request.pastParticiple, difficultyLevel=request.difficultyLevel)
        try:
            verb_key = verb.put()
            verb_saved = verb_key.get().to_dict()
        except:
            raise

        return verb_message(verbId = verb_key.id(), infinitive=verb_saved['infinitive'],
                            pastSimple=verb_saved['pastSimple'], pastParticiple=verb_saved['pastParticiple'],
                            difficultyLevel=verb_saved['difficultyLevel'])

    @endpoints.method(GET_RESOURCE2, EchoResponse, path='verbs/{id}', http_method='DELETE', name='verbs.del')
    def del_verb(self, request):
        """
        Del a verb from the data store.
        :param request:
        :return:
        """

        key = ndb.Key('Verb', long(request.id))
        verb = verb_db_model.query(verb_db_model.key == key).get()

        if verb:
            verb.key.delete()
            return EchoResponse(content='Ok')
        else:
            raise endpoints.NotFoundException('Verb {} not found'.format(request.id))

# [END echo_api]


# [START api_server]
api = endpoints.api_server([IVCheckerApi])
# [END api_server]
