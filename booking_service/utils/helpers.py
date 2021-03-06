from datetime import date as _date, timedelta as _td
from random import sample as _sample
from string import ascii_letters as _letters
from typing import Union, Tuple


TODAY = _date.today()
START_TIME, END_TIME = 9, 17
_used_date, _used_time = TODAY, START_TIME


def random_str(length: int = 10) -> str:
    """Получить случайную строку указанной длины"""
    return ''.join(_sample(_letters, length))


def get_next_date_time(fmt: str = '') -> Tuple[Union[_date, str], int]:
    """Получить следующие валидные дату и время"""
    global _used_date, _used_time

    if _used_date.isoweekday() > 5:
        _used_date += _td(days=2)

    date, time = _used_date, _used_time
    if _used_time == END_TIME:
        _used_date += _td(days=1)
        _used_time = START_TIME
    else:
        _used_time += 1

    if fmt:
        date = date.strftime(fmt)

    return date, time


def get_nearest_day_off() -> _date:
    """Получить дату ближайшей субботы"""

    if TODAY.isoweekday() == 6:
        saturday = TODAY

    elif TODAY.isoweekday() == 7:
        saturday = TODAY + _td(days=6)

    else:
        delta = 6 - TODAY.isoweekday()
        saturday = TODAY + _td(days=delta)

    return saturday
