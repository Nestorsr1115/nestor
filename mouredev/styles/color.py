from enum import Enum

from httpx import head

class Color(Enum):
    Primary="#14A1F0",
    Secondary="#087ec4",
    Background="#0C151D",
    Content="#171F26",
    Rojo="#FF0000"

class TextColor(Enum):
    header="#F1F2F4",
    body="#C3C7CB",
    footer="#A3ABB2",