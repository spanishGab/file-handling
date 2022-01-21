from collections import namedtuple

Exceptions = namedtuple('Exceptions', ['MESSAGES', ])
ErrorMessages = namedtuple('Messages', ['TYPE_ERROR', 'VALUE_ERROR'])

EXCEPTIONS = Exceptions(
    MESSAGES=ErrorMessages(
        TYPE_ERROR=("The '{param}' param must be an instance of '{tp}',"
                    + " got {inst}"),
        VALUE_ERROR=("The '{param}' param must respect the restriction:"
                     + " {restr}"))
)
