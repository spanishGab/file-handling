from collections import namedtuple
from tzlocal import get_localzone_name

DateTimeInfo = namedtuple('DateTimeInfo', ['LOCAL_TIMEZONE',
                                           'FULL_DATETIME_FORMAT'])

CustomExceptions = namedtuple('CustomExceptions', ['MESSAGES', 'NAMES'])
CustomExceptionTypes = namedtuple('CustomExceptionTypes', ['NOT_A_FILE'])

ErrorMessages = namedtuple('Messages', ['TYPE_ERROR',
                                        'VALUE_ERROR',
                                        'NOT_A_FILE_EXCEPTION'])

CUSTOM_EXCEPTIONS = CustomExceptions(
    MESSAGES=ErrorMessages(
        TYPE_ERROR=("The '{param}' param must be an instance of '{tp}',"
                    + " got {inst}"),
        VALUE_ERROR=("The '{param}' param must respect the restriction:"
                     + " {restr}"),
        NOT_A_FILE_EXCEPTION="The given file name doesn't repressent a file."
    ),
    NAMES=CustomExceptionTypes(
        NOT_A_FILE='NotAFileException',
    )
)

DATETIME_INFO = DateTimeInfo(
    LOCAL_TIMEZONE=get_localzone_name(),
    FULL_DATETIME_FORMAT='%Y-%m-%dT%H:%M:%S.%f'
)
