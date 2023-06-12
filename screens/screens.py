from psutil import Process
from vbml import Patcher
from typing import List, Optional, Dict, Any
# > Local Import's
from .units import SCREEN_LS
from .req import screen, check_pattern
from .exceptions import CreateScreenError

class Screen:
    def __init__(self, name: str, *args, **kwargs) -> None:
        self.name = name
        self.id: Optional[int] = kwargs.get("id", None)
        
        if self.id is None:
            if (s:=get_session_by_name(self.name)) is not None:
                self.id: int = s.id
            else:
                try:
                    screen("-dmS", f"\"{name}\"")
                    s: Screen = get_session_by_name(self.name)
                    self.id: int = s.id
                except:
                    raise CreateScreenError()
    
    def __str__(self) -> str:
        return f'ScreenSession(name={repr(self.name)}, id={repr(self.id)})'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def kill(self) -> None:
        if self.id is not None:
            Process(self.id).kill()
            self.id = None
            wipe()
    
    def send_command(self, c: str) -> None:
        if self.id is not None:
            screen("-r", f"\"{self.name}\"", "-X", "stuff", f"\"{c}\r\"")

# ! Other
def wipe() -> None: screen("-wipe")

# ! Get Sessions
def get_sessions_dict() -> List[Dict[str, Any]]:
    patcher, sessions = Patcher(), []
    for line in screen("-ls"):
        if (data:=check_pattern(line, patcher, SCREEN_LS)) is not None:
            sessions.append(data)
    return sessions

def get_sessions() -> List[Screen]:
    return [ Screen(**data) for data in get_sessions_dict() ]

# ! Get Session
def get_session_by_name(name: str) -> Optional[Screen]:
    for i in get_sessions():
        if name == i.name:
            return i

def get_session_by_id(_id: int) -> Optional[Screen]:
    for i in get_sessions():
        if _id == i.id:
            return i
