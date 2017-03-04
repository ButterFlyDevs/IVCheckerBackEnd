from protorpc import messages

class Example(messages.Message):
    example = messages.StringField(1)

class EchoResponse(messages.Message):
    """A proto Message that contains a simple string field."""
    content = messages.StringField(1)

class ID(messages.Message):
    id = messages.StringField(1)

class Verb(messages.Message):

    verbId = messages.IntegerField(1)

    infinitive = messages.StringField(2)
    pastSimple = messages.StringField(3)
    pastParticiple = messages.StringField(4)

    difficultyLevel = messages.IntegerField(5, variant=messages.Variant.INT32)

    examples = messages.MessageField(Example, 6, repeated=True)

class VerbsList(messages.Message):
    verbs = messages.MessageField(Verb, 1, repeated=True)