class CreateScreenError(Exception):
    """Called if screen session creation has failed."""
    def __init__(self, *args: str) -> None:
        """Called if the screen command does not exist."""
        self.msg = "Failed to create a screen-session" if len(args) == 0 else " ".join([str(i) for i in args])
    
    def __str__(self) -> str: return self.msg

class ScreenExistsError(Exception):
    """Called if the screen command does not exist"""
    def __init__(self, *args: str) -> None:
        """Called if the screen command does not exist"""
        self.msg = "Install the 'screen' on your device!" if len(args) == 0 else " ".join([str(i) for i in args])
    
    def __str__(self) -> str: return self.msg