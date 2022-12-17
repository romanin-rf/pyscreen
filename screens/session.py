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
        self.id = id
        self.name = name
        if new:
            for session in get_all_sessions():
                if name == session.name:
                    raise MoreSessionsWithTheSameNameException
            command(f'screen -d -m -S {name}')
            for session in get_all_sessions():
                if session.name == self.name:
                    self.id = session.id

    def send_command(self, _command: str) -> None: command(['screen', '-r', self.name, '-X', 'stuff', f'{_command} \r'])
    def kill(self) -> None: command(f'screen -S {self.name} -X quit')
    def __repr__(self) -> str: return f'<ScreenSession, id={self.id}, name={self.name.__repr__()}>'

def get_all_sessions() -> List[ScreenSession]:
    raw_screens = command('screen -ls', return_output=True)
    screen_sessions = []
    for n, line in enumerate(raw_screens):
        if (n == 0) or (n > len(raw_screens)-3):
            continue
        session, date, attached_state = line.strip().split('\t')
        id, name = session.split('.')
        session = ScreenSession(name, id=int(id), new=False)
        screen_sessions.append(session)
    return screen_sessions

def get_session_with_name(name: str) -> Optional[ScreenSession]:
    for session in get_all_sessions():
        if name == session.name:
            return session
