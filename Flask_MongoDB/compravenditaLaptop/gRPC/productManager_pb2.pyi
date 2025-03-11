from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor

class sellRequest(_message.Message):
    __slots__ = ("id")
    ID_FIELD_NUMBER : _ClassVar[int]
    id : int

    def __init__(self, id: _Optional[int]= ...) -> None: ...

class sellResponse(_message.Message):
    __slots__ = ("success")
    SUCCESS_FIELD_NUMBER : _ClassVar[int]
    success : bool

    def __init__(self, success: _Optional[bool]= ...) -> None: ...

class Empty(_message.Message):
    _slots__=()

    def __init__(self)->None:...

class buyResponse(_message.Message):
    __slots__ = ("id")
    ID_FIELD_NUMBER : _ClassVar[int]
    id : int

    def __init__(self, id: _Optional[int]= ...) -> None: ...
    
