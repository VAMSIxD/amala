from typing import Union, List
from pyrogram import filters
from config import COMMAND_PREFIXES

other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)

def get_command(value: str) -> List:
    return commands["command"][value]

