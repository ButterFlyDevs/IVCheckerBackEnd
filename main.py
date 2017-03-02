"""This is ivchecker API implemented using Google Cloud
Endpoints."""

# [START imports]
import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote
# [END imports]


# [START messages]
class EchoRequest(messages.Message):
    content = messages.StringField(1)


class EchoResponse(messages.Message):
    """A proto Message that contains a simple string field."""
    content = messages.StringField(1)

# [END messages]


# [START echo_api]
@endpoints.api(name='ivchecker', version='v1')
class EchoApi(remote.Service):

    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        message_types.VoidMessage,
        # This method returns an EchoResponse message.
        EchoResponse,
        path='helloWorld',
        http_method='GET',
        name='echo_api_key')
    def echo_api_key(self, request):
        return EchoResponse(content='Hello World!')

# [END echo_api]


# [START api_server]
api = endpoints.api_server([EchoApi])
# [END api_server]
