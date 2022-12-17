from .command import command
from typing import List

class MoreSessionsWithTheSameNameException(Exception): pass

class ScreenSession():
    id = None
    def __init__(
        self,
        name: str,
        new: bool=True
    ) -> None:
        self.name = name
        if new:
            for session in get_all_sessions():
                if name == session.name:
                    raise MoreSessionsWithTheSameNameException
            command('screen -d -m -S '+name)
            for session in get_all_sessions():
                if session.name == self.name:
                    self.id = session.id

    def send_command(self, _command: str) -> None: command(['screen', '-r', self.name, '-X', 'stuff', _command+' \r'])
    def kill(self) -> None: command(f'screen -S {self.name.__repr__()} -X quit')
    def __repr__(self) -> str: return f'<ScreenSession, id={str(self.id).__repr__()}, name={self.name.__repr__()}>'

def get_all_sessions() -> List[ScreenSession]:
    raw_screens = command('screen -ls', return_output=True)
    screen_sessions = []
    for n, line in enumerate(raw_screens):
        if (n == 0) or (n > len(raw_screens)-3):
            continue
        session, date, attached_state = line.strip().split('\t')
        id, name = session.split('.')
        session = ScreenSession(name, new=False)
        session.id = int(id)
        screen_sessions.append(session)
    return screen_sessions

def get_session_with_name(name: str):
    for session in get_all_sessions():
        if name == session.name:
            return session
