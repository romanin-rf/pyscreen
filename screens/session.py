from .command import command
from typing import List, Optional

class MoreSessionsWithTheSameNameException(Exception): pass

class ScreenSession():
    def __init__(
        self,
        name: str,
        *,
        id: Optional[int]=None,
        new: bool=True
    ) -> None:
        self.id: int = id
        self.name: str = name
        if new:
            if not exists_session(self.name):
                command(f'screen -d -m -S {name}')
            for i in get_all_sessions():
                if i.name == self.name:
                    self.id = i.id
                    self.name = i.name
                    break

    def send_command(self, _command: str) -> None: command(['screen', '-r', self.name, '-X', 'stuff', f'{_command} \r'])
    def kill(self) -> None: command(f'screen -S {self.name} -X quit')
    def __repr__(self) -> str: return f'<ScreenSession, id={self.id}, name={self.name.__repr__()}>'

def exists_session(name: str) -> bool:
    for i in get_all_sessions():
        if i.name == name:
            return True
    return False

def get_all_sessions() -> List[ScreenSession]:
    raw_screens = command('screen -ls', return_output=True)
    screen_sessions = []
    for n, line in enumerate(raw_screens):
        if (n == 0) or (n > len(raw_screens)-3):
            continue
        session, date, attached_state = line.strip().split(b'\t')
        id, name = session.split(b'.')
        session = ScreenSession(name.decode(errors="ignore"), id=int(id), new=False)
        screen_sessions.append(session)
    return screen_sessions

def get_session_by_name(name: str) -> Optional[ScreenSession]:
    for session in get_all_sessions():
        if name == session.name:
            return session

def get_session_by_id(_id: int) -> Optional[ScreenSession]:
    for session in get_all_sessions():
        if _id == session.id:
            return session
