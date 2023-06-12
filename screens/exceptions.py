class CreateScreenError(Exception):
    """Called if screen session creation has failed."""
    def __init__(self, *args: str) -> None:
        """Called if the screen command does not exist."""
        if len(args) > 0: self.args = args
        else: self.args = ("Failed to create a screen-session.",)

class ScreenExistsError(Exception):
    """Called if the screen command does not exist"""
    def __init__(self, *args: str) -> None:
        """Called if the screen command does not exist"""
        if len(args) > 0: self.args = args
        else: self.args = ("Install the 'screen' on your device!",)
