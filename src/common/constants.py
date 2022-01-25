from collections import namedtuple
from tzlocal import get_localzone_name
from pytz import timezone

DateTimeInfo = namedtuple('DateTimeInfo', ['LOCAL_TIMEZONE', ])
Exceptions = namedtuple('Exceptions', ['MESSAGES', ])
ErrorMessages = namedtuple('Messages', ['TYPE_ERROR', 'VALUE_ERROR'])

EXCEPTIONS = Exceptions(
    MESSAGES=ErrorMessages(
        TYPE_ERROR=("The '{param}' param must be an instance of '{tp}',"
                    + " got {inst}"),
        VALUE_ERROR=("The '{param}' param must respect the restriction:"
                     + " {restr}"))
)

DATETIME_INFO = DateTimeInfo(
    LOCAL_TIMEZONE=timezone(get_localzone_name())
)
