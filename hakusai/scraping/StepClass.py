from typing import Literal, TypedDict


class Step(TypedDict):
    num: int
    xpath: str
    action: Literal['click', 'insert', 'insert_and_enter']
    value: str
